from dataclasses import field
from rest_framework import serializers
from .models import Event, Organizer

class OrganizerSerialier(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = (
            'pk',
            'name',
            'address',
            'description',
        )

class EventSerializer (serializers.ModelSerializer):
    organizers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Event
        fields = (
            'pk',
            'title',
            'start_date_time',
            'end_date_time',
            'location',
            'organizers',
        )