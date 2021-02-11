from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('zone/<slug:slug>/', views.parking_status, name='parkingzone-detail'),

]