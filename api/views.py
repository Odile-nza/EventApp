from datetime import datetime
from django.http import Http404
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EventSerializer, OrganizerSerializer, EventUpdateSerializer, OrganizersOfEventSerializer
from .models import Event, Organizer
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
    events = Event.objects.all()
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
    event.delete()
    return Response({'message': 'Event was deleted successfully!'}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def RateEvent(request):
    try:
        events = Event.objects.filter(start_date_time__gte=datetime(2022,5,1),
                                      end_date_time__lte=datetime(2022,5,30))
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    except Event.DoesNotExist:
        raise Http404("Given range not found")
    

@api_view(['GET'])
def CloseEvent(request,pk):
    try:
        event = Event.objects.get(code=pk)
        event.status = "CLOSED"
        event.save()
        return Response(data={'message':"status changed successfully"},status=status.HTTP_202_ACCEPTED)
    except Event.DoesNotExist:
        raise Http404("Given event not found")

@api_view(['GET'])
def AllOrganizersEvent(request,pk):
    event = Event.objects.get(code=pk)
    organizers = event.organizers.all()
    serializer = OrganizerSerializer(organizers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def SetOrganizersEvent(request,pk):
    event = Event.objects.get(code=pk)
    serializer = OrganizersOfEventSerializer(data=request.data)
    organizer = request.data['organizers']
    for org in list:
        org = organizer.byid(org)
        eventOrg = org()
        eventOrg.Event = event
        return Response(serializer.data)

    

    

    