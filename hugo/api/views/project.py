from django.shortcuts import render
from rest_framework import   status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from hugo.db.models import Project, User
from hugo.api.serializers import ProjectSerializer

class ProjectList(APIView):
    """
    A view for viewing List of Project
    """
    def get(self,request, format=None):
        
       projects = Project.objects.all()
       serializer = ProjectSerializer(projects, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = ProjectSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    """
    Retrieve, update or delete a Project instance.
    """
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Projects
        """
        projects = self.get_object(pk)
        serializer = ProjectSerializer(projects)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = ProjectSerializer( data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=pk)
            request.data["user"]= user.id
            print(pk)
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response({"message":" user does not exist"}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        projects = self.get_object(pk)
        projects.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)