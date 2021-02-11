from django.shortcuts import render

from parking_zones.models import Parking_Zone



def index(request):
    context = {
        'all_parking_zones':Parking_Zone.objects.all()
    }
    return render(request, 'source/index.html', context)


def parking_status(request, slug):
    all_parking_zones = Parking_Zone.objects.all()
    parking_zone = all_parking_zones.get(slug=slug)
    vacant_slots = int(parking_zone.num_of_slots) - int(parking_zone.occupied_slots)
    context = {
        'parking_zone': parking_zone,
        'vacant_slots':vacant_slots 
    }
    return render(request, 'source/status.html', context)
