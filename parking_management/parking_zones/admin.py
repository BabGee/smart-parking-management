from django.contrib import admin

from .models import Parking_Zone, Reservation

class Parking_ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_of_slots','occupied_slots', 'vacant_slots', 'address', 'price',)
    list_filter = ('address',)
    prepopulated_fields = {'slug': ('name',)}


class Reservation_Admin(admin.ModelAdmin):
    list_display = ('customer', 'start_date', 'finish_date', 'parking_zone', 'plate_number', 'phone_number',)
    list_filter = ('start_date', 'finish_date', 'parking_zone')
    search_fields = ('customer', 'plate_number',)



admin.site.register(Parking_Zone, Parking_ZoneAdmin)
admin.site.register(Reservation, Reservation_Admin)
