from django.shortcuts import render
from .models import Table, Reservation
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import CreateView

def base(request):
    return render(request, 'tablebooking/base.html')

def createbooking(CreateView):
    model = Reservation
    template_name = "createbooking.html"

def booking_form(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        #table = Table.object.filter(table_no=)
        number_of_people = request.POST['number_of_people']
        number_of_child_seats = request.POST['number_of_child_seats']
        private_booth = request.POST['private_booth']
        print(request.POST['private_booth'])
        user = request.user 
        check_availability()
        #new_reservation = Reservation(user=user, private_booth=private_booth, date=date, time=time, number_of_people=number_of_people, number_of_child_seats=number_of_child_seats)
        #new_reservation.save()
    return render(request, 'tablebooking/booking_form.html')

'''def validate_date():
    date = Reservation.objects.get('date')
    date_format = '%Y-%m-%d'
    today = datetime.today()
    if (date == ""):
        raise Validation_Error ("This field cannot be left blank")
        if (date < today):
            raise Validation_Error ("Booking date can't be in the past")
                else
                    try:
                        dateObject = datetime.datetime.strptime(date_string, date_format)
                        print(dateObject)
                    except ValueError:
                        print("Incorrect data format, should be YYYY-MM-DD")  
    return date


validate_date()


def validate_time():
    time = Reservation.objects.get('time')
    time_format = "%H:%M"
    if (time = ""):
        raise Validation_Error ("This field cannot be left blank")
        if (time < "09:00" or time > "20:00"):
            raise Validation_Error ("Booking time is outside of the opening hours")      
    return time



validate_time()


def validate_number_of_people():
    number_of_people = Table.objects.get('number_of_people')
    if (number_of_people = "")
        raise Validation_Error ("This field cannot be left blank")
            if (number_of_people < 1 or number_of_people > 6)
                raise Validation_Error ("Sorry, we don't have a table for that number of people")
    return number_of_people


validate_number_of_people()


def validate_number_of_child_seats():
    number_of_child_seats = Table.objects.get('number_of_child_seats')
    if (number_of_child_seats = "")
        raise Validation_Error ("This field cannot be left blank")
            if (number_of_people < 0 or number_of_people > 3)
                raise Validation_Error ("Sorry, we don't have that number of child seats")
    return number_of_child_seats


validate_number_of_people()


def check_availability(date, time, number_of_people):
    avail_list = []
    number_of_people = Table.objects.get('number_of_people')
    reservation_list = [Reservation.object.filter('date', 'time'), number_of_people]
    for Reservation in reseration_list:
        if (Reservation.date = date and Reservation.time = time and Table.number_of_people = number_of_people):
            raise Validation_Error ("Sorry, we don't have a table available for your required time, date and number of people. Do you want to be waitlisted?")
                #if (yes)
                #    waitlisted == True
                #else
                #    waitlisted == False
        else
            new_reservation = Reservation(user=user, private_booth=private_booth, date=date, time=time, number_of_people=number_of_people, number_of_child_seats=number_of_child_seats)
            new_reservation.save()
return new_reservation
    

#def block_time ():
    ## for selected time 2hours need to be blocked
'''

def login(request):
    return render(request, 'tablebooking/menu.html')


def manage_booking(request):
    return render(request, 'tablebooking/manage_booking.html')
