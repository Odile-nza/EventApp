from multiprocessing import Event
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed")
    return value

unique_event_title = UniqueValidator(queryset=Event.objects.all(), lookup='iexact')