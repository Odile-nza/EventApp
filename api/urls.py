from django import urls
from django.urls import path
from . import views

urlpatterns = [

 path('organizers-list/', views.AllOrganizers, name='organizers-list'),
 path('organizer-detail/<int:pk>/', views.ViewOrganizer, name='organizer-detail'),
 path('organizer-create/', views.CreateOrganizer, name='organizer-create'),
 path('organizer-update/<int:pk>/', views.UpdateOrganiser, name='organizer-update'),
 path('organizer-delete/<int:pk>/', views.DeleteOrganizer, name='organizer-delete'),

 path('events-list/', views.AllEvents, name='events-list'),
 path('event-detail/<int:pk>/', views.ViewEvent, name='event-detail'),
 path('event-create/', views.CreateEvent, name='event-create'),
 path('event-update/<int:pk>/', views.UpdateEvent, name='event-update'),
 path('event-delete/<int:pk>/', views.DeleteEvent, name='event-delete'),

 path('event-rateDate/', views.RateEvent, name='event-rateDate'),
 
]