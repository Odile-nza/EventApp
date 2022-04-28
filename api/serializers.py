from dataclasses import field, fields
from rest_framework import serializers
from .models import Event, Organizer


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = (
            'org_id',
            'name',
            'address',
            'description',
        )

class EventSerializer (serializers.ModelSerializer):
    organizers = serializers.PrimaryKeyRelatedField( many=True, read_only=True)
    class Meta:
        model = Event
        fields = (
            'title',
            'code',
            'start_date_time',
            'end_date_time',
            'location',
            'organizers',
            'status',
        )

class EventUpdateSerializer (serializers.ModelSerializer):
    organizers = serializers.PrimaryKeyRelatedField( many=True, read_only=True)
    class Meta:
        model = Event
        fields = (
            'title',
            'start_date_time',
            'end_date_time',
            'location',
            'organizers',
            'status',
        )

class OrganizersOfEventSerializer (serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        fields = (
            'event',
            'organizers',
        )

           