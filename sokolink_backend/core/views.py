from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@csrf_exempt
@csrf_exempt
def ussd_callback(request):
    from .models import Farmer, Product

    session_id = request.POST.get('sessionId')
    service_code = request.POST.get('serviceCode')
    phone_number = request.POST.get('phoneNumber')
    text = request.POST.get('text')

    user_response = text.split("*") if text else []

    response = "END An error occurred."

    if len(user_response) == 0:
        response = "CON Welcome to SokoLink!\n1. Register\n2. View/Post Products\n3. Search Market"

    # Registration
    elif len(user_response) == 2 and user_response[0] == "1":
        name = user_response[1]
        Farmer.objects.update_or_create(phone_number=phone_number, defaults={"name": name})
        response = f"END Thank you {name}, you're now registered!"

    elif user_response[0] == "1":
        response = "CON Enter your full name:"

    # Option 2: View/Post Products
    elif user_response[0] == "2" and len(user_response) == 1:
        response = "CON What would you like to do?\n1. View my products\n2. Post new product"

    # View products
    elif user_response[0:2] == ["2", "1"]:
        try:
            farmer = Farmer.objects.get(phone_number=phone_number)
            products = Product.objects.filter(farmer=farmer).order_by("-created_at")[:3]
            if products:
                product_list = "\n".join([f"{p.name} ({p.quantity} @ KES {p.price})" for p in products])
                response = f"END Your products:\n{product_list}"
            else:
                response = "END You have no products listed."
        except Farmer.DoesNotExist:
            response = "END You must register first using option 1."

    # Start product posting flow
    elif user_response[0:2] == ["2", "2"] and len(user_response) == 2:
        response = "CON Enter product name:"

    elif user_response[0:2] == ["2", "2"] and len(user_response) == 3:
        response = "CON Enter quantity (in units):"

    elif user_response[0:2] == ["2", "2"] and len(user_response) == 4:
        response = "CON Enter price per unit (KES):"

    elif user_response[0:2] == ["2", "2"] and len(user_response) == 5:
        try:
            farmer = Farmer.objects.get(phone_number=phone_number)
            name = user_response[2]
            quantity = int(user_response[3])
            price = float(user_response[4])
            Product.objects.create(farmer=farmer, name=name, quantity=quantity, price=price)
            response = f"END {name} posted successfully!"
        except Exception as e:
            response = f"END Failed to save product."

    # Option 3: Search Market (show latest products)
    elif user_response[0] == "3":
        products = Product.objects.all().order_by("-created_at")[:5]
        if products:
            product_list = "\n".join([f"{p.name} ({p.quantity} @ {p.price})" for p in products])
            response = f"END Market Listings:\n{product_list}"
        else:
            response = "END No products found."

    return HttpResponse(response, content_type='text/plain')
