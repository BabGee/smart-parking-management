from django.db import models   
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Parking_Zone(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    num_of_slots = models.PositiveIntegerField()
    occupied_slots = models.PositiveIntegerField(null=True, blank=True, default=0)
    vacant_slots = models.PositiveIntegerField(null=True, blank=True, default=0)
    address = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('parkingzone-detail', kwargs={
            'slug': self.slug
        })     



class Reservation(models.Model):
    ticket_code = models.CharField(max_length=6, blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()
    parking_zone = models.ForeignKey(Parking_Zone, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=16)
    checked_out = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Reservation for vehicle: {self.plate_number}'