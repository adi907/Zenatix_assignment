"""
URL configuration for event_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from events.views import (
    EventListCreateView, EventRetrieveUpdateDeleteView,
    RegistrationListCreateView, RegistrationRetrieveUpdateDeleteView,
    VenueListCreateView, VenueRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventRetrieveUpdateDeleteView.as_view(), name='event-detail'),
    path('registrations/', RegistrationListCreateView.as_view(), name='registration-list'),
    path('registrations/<int:pk>/', RegistrationRetrieveUpdateDeleteView.as_view(), name='registration-detail'),
    path('venues/', VenueListCreateView.as_view(), name='venue-list'),
    path('venues/<int:pk>/', VenueRetrieveUpdateDeleteView.as_view(), name='venue-detail'),
]
