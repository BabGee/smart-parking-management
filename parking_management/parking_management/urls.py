"""parking_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from parking_zones import views as parkingzoneviews
from users import views as users_views

urlpatterns = [
    path('', include('source.urls')),
    path('admin/', admin.site.urls),
    path('user/signup/', users_views.signup_view, name='signup'),
    path('user/login', users_views.user_login, name='login'),
    path('user/logout/', users_views.user_logout, name='logout'),
    path('book/', login_required(parkingzoneviews.ReservationView.as_view()), name='book'),
    path('ticket/', login_required(parkingzoneviews.Ticket_Pdf.as_view()), name='ticket'),
    path('all_tickets/', login_required(parkingzoneviews.Display_Tickets.as_view()), name='all-tickets'),
    path('checkout/', parkingzoneviews.check_out, name='checkout')
    ]
