from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='home'),
    #path('booking_form/', views.booking_form, name='booking_form'),
    path('booking_form/', views.createbooking, name='createbooking'),
    path('menu/', views.login, name='menu'),
    path('manage_booking/', views.manage_booking, name='manage_booking'),
]
