from django.contrib import admin

from .models import Parking_Zone, Reservation

class Parking_ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_of_slots','occupied_slots', 'vacant_slots', 'address', 'price',)
    list_filter = ('address',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class Reservation_Admin(admin.ModelAdmin):
    list_display = ('ticket_code', 'customer', 'start_date', 'finish_date', 'parking_zone', 'plate_number', 'phone_number', 'checked_out')
    list_filter = ('start_date', 'finish_date', 'parking_zone', 'checked_out')
    search_fields = ('ticket_code', 'plate_number')



admin.site.register(Parking_Zone, Parking_ZoneAdmin)
admin.site.register(Reservation, Reservation_Admin)
