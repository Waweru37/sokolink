from django.contrib import admin
from django.urls import path
from core.views import ussd_callback
from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('ussd/', ussd_callback),
]
