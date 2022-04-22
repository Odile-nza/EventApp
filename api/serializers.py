from dataclasses import field, fields
from rest_framework import serializers
from .models import Event, Organizer, Ratedate

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

class RatedateSerializer (serializers.ModelSerializer):
    class Meta:
        model = Ratedate
        fields = (
            'pk',
            'date_gte',
            'date_lte',
        )