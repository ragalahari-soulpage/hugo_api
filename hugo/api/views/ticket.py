from hugo.db.models import Ticket, RequestTicket, TicketAvailability
from hugo.api.serializers import TicketSerializer, RequestTicketSerializer, TicketAvailabilitySerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import   status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TicketList(APIView):
    """
    A view for viewing List of Tickets
    """
    def get(self,request, format=None):
        
       tickets = Ticket.objects.all()
       serializer = TicketSerializer(tickets, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = TicketSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetail(APIView):
    """
    Retrieve, update or delete a Ticket instance.
    """
    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Event
        """
        tickets = self.get_object(pk)
        serializer = TicketSerializer(tickets)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = TicketSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        tickets = self.get_object(pk)
        tickets.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)


class RequestTicketList(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

           req = RequestTicket.objects.filter(id=pk)
           serializer = RequestTicketSerializer(req, many=True)
           return Response(serializer.data)

    def post(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        request.data["ticket"]= ticket.id
        print(pk)
        print(request.data)
        serializer = RequestTicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
            try:
              return RequestTicket.objects.get(pk=pk)
            except RequestTicket.DoesNotExist:
             raise Http404

    def put(self, request, pk, format=None):
        
        ticket = Ticket.objects.get(id=pk)
        request.data["ticket"]= ticket.id
        req = self.get_object(pk)
        serializer = RequestTicketSerializer(req ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk, format=None):
        req = self.get_object(pk)
        req.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)

class RequestTicketDetail(APIView):
    """
    A view for viewing List of Request Tickets
    """
    def get(self,request, format=None):
        
       req = RequestTicket.objects.all()
       serializer = RequestTicketSerializer(req, many=True)
       return Response(serializer.data)

class TicketAvailabilityList(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

           availability = TicketAvailability.objects.filter(id=pk)
           serializer = TicketAvailabilitySerializer(availability, many=True)
           return Response(serializer.data)

    def post(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        request.data["ticket"]= ticket.id
        print(pk)
        print(request.data)
        serializer = TicketAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
            try:
              return TicketAvailability.objects.get(pk=pk)
            except TicketAvailability.DoesNotExist:
             raise Http404

    def put(self, request, pk, format=None):
        
        ticket = Ticket.objects.get(id=pk)
        request.data["ticket"]= ticket.id
        availability = self.get_object(pk)
        serializer = TicketAvailabilitySerializer(availability,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk, format=None):
        availability = self.get_object(pk)
        availability.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)

class TicketAvailabilityDetail(APIView):
    """
    A view for viewing List of  Tickets availability
    """
    def get(self,request, format=None):
        
       availability = TicketAvailability.objects.all()
       serializer = TicketAvailabilitySerializer(availability, many=True)
       return Response(serializer.data)
