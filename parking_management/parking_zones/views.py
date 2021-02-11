from django.shortcuts import render, redirect
from django.views import View
from .models import Reservation, Parking_Zone
from django.db.models import Q
from django.contrib import messages
from .forms import ReservationForm


class ReservationView(View):
    def get(self, request):
        reservation = ReservationForm()

        return render(request, 'parking_zones/booking.html', {'form': reservation})

    def post(self, request):
        reservation_form = ReservationForm(data=request.POST)

        if reservation_form.is_valid():
            start_date = reservation_form.cleaned_data['start_date']
            finish_date = reservation_form.cleaned_data['finish_date']
            parking_zone = reservation_form.cleaned_data['parking_zone']
            plate_number = reservation_form.cleaned_data['plate_number']

            if Reservation.objects.filter(Q(plate_number=plate_number,
                                            start_date__range=[start_date, finish_date]) |
                                          Q(plate_number=plate_number,
                                            finish_date__range=[start_date, finish_date])).exists():
                                            messages.warning(request, 'Dates overlaps. Try other dates and / or parking space.')
                
            else:
                reservation = reservation_form.save(commit=False)
                reservation.customer = request.user
                reservation.parking_zone = parking_zone
                reservation.save()
                #print(parking_zone) #River Mall
                parkingzone = Parking_Zone.objects.get(name=parking_zone)
                parkingzone.occupied_slots += 1
                parkingzone.save()
                vacantslots = int(parkingzone.num_of_slots) - int(parkingzone.occupied_slots)
                parkingzone.vacant_slots = vacantslots
                parkingzone.save()
                messages.info(request, 'Successfully Booked')
                return redirect('index')

            return render(request, 'parking_zones/booking.html', {'form': reservation_form})

        return render(request, 'parking_zones/booking.html', {'form': reservation_form})
