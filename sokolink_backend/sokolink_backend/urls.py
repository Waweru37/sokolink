from django.contrib import admin
from django.urls import path
from core.views import ussd_callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ussd/', ussd_callback),
]
