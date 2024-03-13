from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight , Airport,Passenger
from datetime import datetime
from datetime import datetime

# Create your views here.

def index(request):
    today = datetime.today().strftime('%Y-%m-%d')
    return render(request,'flights/index.html',{
        'date':today,
        "flights": Flight.objects.all()
    })


def flight(request,flight_id):
    flights = Flight.objects.all()
    flight_ids = [flight.id for flight in flights]
    for flight in flights:
        if flight_id not in flight_ids:     #Error checking
            return render(request,'flights/error.html',{
                "message": f'Currently have no flight for Flight id: {flight_id}'
            })
        else:
            flight = Flight.objects.get(pk=flight_id)
            return render(request,'flights/flight.html',{
                "flight":flight,
                "passengers":flight.Passengers.all(),
                'non_passengers':Passenger.objects.exclude(flights = flight).all() #exclude all passengers that already on this flight
            })
'''
    getting list of ids

    flight_ids = [flight.id for flight in Flight.objects.all()]
    print(flight_ids)
'''

def book(request,flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id) #get the current flight
        passenger = Passenger.objects.get(pk = int(request.POST['passenger']))  #get the passenger from form
        passenger.flights.add(flight)   #add flight to flights in passenger
        return HttpResponseRedirect(reverse('flight',args=(flight.id,)))