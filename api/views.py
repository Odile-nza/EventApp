from datetime import datetime
import datetime as dt
from typing import List
from django.http import Http404
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EventSerializer, OrganizerSerializer, EventUpdateSerializer, OrganizersOfEventSerializer
from .models import Event, Organizer, OrganizersOfEvent
from rest_framework import status


@api_view(['GET'])
def AllOrganizers(request):
    organizers = Organizer.objects.all()
    serializer = OrganizerSerializer(organizers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewOrganizer(request,pk):
    organizer = Organizer.objects.get(org_id=pk)
    serializer = OrganizerSerializer(organizer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateOrganizer(request):
    serializer = OrganizerSerializer(data=request.data)
    if Organizer.objects.filter(org_id=request.data['org_id']).exists():
      raise serializers.ValidationError('This organizer already exists')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def UpdateOrganiser(request,pk):
    organizer = Organizer.objects.get(id=pk)
    serializer = OrganizerSerializer(instance=organizer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def DeleteOrganizer(request,pk):
    organizer = Organizer.objects.get(id=pk)
    if organizer.delete():
       return Response({'message': 'Organizer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def AllEvents(request):
    #events = Event.objects.all()
    events = Event.objects.filter(isDeleted=False)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewEvent(request,pk):
    try:
        event = Event.objects.get(code=pk)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    except Event.DoesNotExist:
        raise Http404("Given event not found")

@api_view(['POST'])
def CreateEvent(request):
    serializer = EventSerializer(data=request.data)
    if Event.objects.filter(code=request.data['code']).exists():
      raise serializers.ValidationError('This data already exists')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def UpdateEvent(request,pk):
    event = Event.objects.get(code=pk)
    serializer = EventUpdateSerializer(instance=event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'message': 'Event  was not updated'},status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def DeleteEvent(request,pk):
    event = Event.objects.get(code=pk)
    event.isDeleted = True
    event.save()
    return Response({'message': 'Event was deleted successfully!'}, status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def RestoreEvent(request,pk):
    event = Event.objects.get(code=pk)
    event.isDeleted = False
    event.save()
    return Response({'message': 'Event was restored successfully!'}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def AllOrganizersEvent(request,pk):
    event = Event.objects.get(code=pk)
    organizers = event.organizers.all()
    serializer = OrganizerSerializer(organizers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def SetOrganizersEvent(request,pk):
    try:
        event_obj = Event.objects.get(id=pk)
        eventOrganizer = request.data["organizer"]
        for org in eventOrganizer:
            print (org)
            org_obj = Organizer.objects.get(org_id=org)
            evog=OrganizersOfEvent()
            evog.organizer=org_obj
            evog.event=event_obj
            evog.save()
        return Response({'message': 'Organizer was assigned successfully!'}, status=status.HTTP_202_ACCEPTED)

    except Event.DoesNotExist:
        raise Http404("Given event not found")

@api_view(['POST'])
def openOrCloseEvent(request,pk):
        event = Event.objects.get(code=pk)
        openOrClose = request.data["status"]
        print(openOrClose)
        event.status= openOrClose
        event.save()
        return Response({'message': 'Status changed successfully!'}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def RangeEvent(request):
    try:
        events = Event.objects.filter(start_date_time__gte=dt.datetime.strptime(request.data["startDate"],"%Y-%m-%d").date(),
                                      end_date_time__lte=dt.datetime.strptime(request.data["endDate"],"%Y-%m-%d").date())
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    except Event.DoesNotExist:
        raise Http404()
