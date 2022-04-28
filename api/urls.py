from django import urls
from django.urls import path
from . import views

urlpatterns = [

 path('organizers-list/', views.AllOrganizers, name='organizers-list'),
 path('organizer-detail/<str:pk>/', views.ViewOrganizer, name='organizer-detail'),
 path('organizer-create/', views.CreateOrganizer, name='organizer-create'),
 path('organizer-update/<str:pk>/', views.UpdateOrganiser, name='organizer-update'),
 path('organizer-delete/<int:pk>/', views.DeleteOrganizer, name='organizer-delete'),

 path('events-list/', views.AllEvents, name='events-list'),
 path('event-detail/<str:pk>/', views.ViewEvent, name='event-detail'),
 path('event-create/', views.CreateEvent, name='event-create'),
 path('event-update/<str:pk>/', views.UpdateEvent, name='event-update'),
 path('event-delete/<str:pk>/', views.DeleteEvent, name='event-delete'),

 path('event-rangeDate/', views.RateEvent, name='event-rangeDate'),
 path('event-close/<str:pk>/',views.CloseEvent, name='event-close'),
 path('event-organizers/<str:pk>/',views. AllOrganizersEvent, name='event-organizers'),
 path('event-setOrganizers/<str:pk>/',views. AllOrganizersEvent, name='event-setOrganizers'),
]