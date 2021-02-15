from django.shortcuts import render, redirect

from parking_zones.models import Parking_Zone, Reservation

from django.contrib import messages

def index(request):  
    context = {
        'all_parking_zones':Parking_Zone.objects.all()
    }
    return render(request, 'source/index.html', context)


def parking_status(request, slug):
    all_parking_zones = Parking_Zone.objects.all()
    parking_zone = all_parking_zones.get(slug=slug)
    context = {
        'parking_zone': parking_zone,
    }
    return render(request, 'source/status.html', context)
