from hugo.db.models import Event, Holiday
from hugo.api.serializers import EventSerializer, HolidaySerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import   status
from rest_framework.response import Response

class EventList(APIView):
    """
    A view for viewing List of Event
    """
    def get(self,request, format=None):
        
       events = Event.objects.all()
       serializer = EventSerializer(events, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = EventSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    """
    Retrieve, update or delete a Event instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Event
        """
        events = self.get_object(pk)
        serializer = EventSerializer(events)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = EventSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        events = self.get_object(pk)
        events.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)


class HolidayList(APIView):
    """
    A view for viewing List of Holiday
    """
    def get(self,request, format=None):
        
       holidays = Holiday.objects.all()
       serializer = HolidaySerializer(holidays, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = HolidaySerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HolidayDetail(APIView):
    """
    Retrieve, update or delete a Holiday instance.
    """
    def get_object(self, pk):
        try:
            return Holiday.objects.get(pk=pk)
        except Holiday.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Holiday
        """
        holidays = self.get_object(pk)
        serializer = HolidaySerializer(holidays)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = HolidaySerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        holidays = self.get_object(pk)
        holidays.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)
