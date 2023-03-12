from django.shortcuts import render
from .models import Table, Reservation
from django.http import HttpResponse
from datetime import datetime

def base(request):
    return render(request, 'tablebooking/base.html')


def booking_form(request):
    if request.method == 'POST':
        print(request.POST['private_booth'])
        private_booth = request.POST['private_booth']
        date = request.POST['date']
        time = request.POST['time']
        number_of_people = request.POST['number_of_people']
        number_of_child_seats = request.POST['number_of_child_seats']
        #table = Table.object.filter(table_no=)
        user = request.user 
        new_reservation = Reservation(user=user, private_booth=private_booth, date=date, time=time, number_of_people=number_of_people, number_of_child_seats=number_of_child_seats)
        new_reservation.save()
    return render(request, 'tablebooking/booking_form.html')


def login(request):
    return render(request, 'tablebooking/menu.html')


def manage_booking(request):
    return render(request, 'tablebooking/manage_booking.html')
