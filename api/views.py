from datetime import date, datetime
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import EventSerializer, OrganizerSerialier, RatedateSerializer
from .models import Event, Organizer, Ratedate
from rest_framework import status




@api_view(['GET'])
def AllOrganizers(request):
    organizers = Organizer.objects.all()
    serializer = OrganizerSerialier (organizers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewOrganizer(request,pk):
    organizer = Organizer.objects.get(id=pk)
    serializer = OrganizerSerialier(organizer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateOrganizer(request):
    serializer = OrganizerSerialier(data=request.data)
    if Organizer.objects.filter(**request.data).exists():
      raise serializers.ValidationError('This organizer already exists')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def UpdateOrganiser(request,pk):
    organizer = Organizer.objects.get(id=pk)
    serializer = OrganizerSerialier(instance=organizer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def DeleteOrganizer(request,pk):
    organizer = Organizer.objects.get(id=pk)
    if organizer.delete():
       return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def AllEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewEvent(request,pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateEvent(request):
    serializer = EventSerializer(data=request.data)
    if Event.objects.filter(**request.data).exists():
      raise serializers.ValidationError('This data already exists')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def UpdateEvent(request,pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def DeleteEvent(request,pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def RateEvent(request):
    events = Event.objects.filter(start_date_time__gte=datetime(2022,4,1),
                                  end_date_time__lte=datetime(2022,4,30))
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)
   