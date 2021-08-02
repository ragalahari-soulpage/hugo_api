from django.shortcuts import render
from rest_framework import   status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from hugo.db.models import Employee, Employment, EmployeeDocs, Education, EducationDocs, Internship
from hugo.api.serializers import (EmployeeSerializer, 
EmploymentSerializer, EmployeeDocsSerializer,
 EducationSerializer, EducationDocsSerializer, InternshipSerializer)


class EmployeeList(APIView):
    """
    A view for viewing List of Employee
    """
    def get(self,request, format=None):
        
       employee = Employee.objects.all()
       serializer = EmployeeSerializer(employee, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = EmployeeSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    """
    Retrieve, update or delete a employee instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Employee
        """
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)


class EmploymentList(APIView):
    """
    A view for viewing List of Employment
    """
    def get(self,request, format=None):
        
       employment = Employment.objects.all()
       serializer = EmploymentSerializer(employment, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = EmploymentSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmploymentDetail(APIView):
    """
    Retrieve, update or delete a employment instance.
    """
    def get_object(self, pk):
        try:
            return Employment.objects.get(pk=pk)
        except Employment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Employment
        """
        employment = self.get_object(pk)
        serializer = EmploymentSerializer(employment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employment = self.get_object(pk)
        serializer = EmploymentSerializer(employment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employment = self.get_object(pk)
        employment.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)

class EmployeeDocsView(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

           document = EmployeeDocs.objects.filter(id=pk)
           serializer = EmployeeDocsSerializer(document, many=True)
           return Response(serializer.data)

    def post(self, request, pk=None):
        employment = Employment.objects.get(id=pk)
        request.data["employment"]= employment.id
        print(pk)
        print(request.data)
        serializer = EmployeeDocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
            try:
              return EmployeeDocs.objects.get(pk=pk)
            except EmployeeDocs.DoesNotExist:
             raise Http404

    def put(self, request, pk, format=None):
        
        employment = Employment.objects.get(id=pk)
        request.data["employment"]= employment.id
        employeedocs = self.get_object(pk)
        serializer = EmployeeDocsSerializer(employeedocs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)

class EmployeedocsList(APIView):
    """
    A view for viewing List of Employeedocs
    """
    def get(self,request, format=None):
        
       employeedocs = EmployeeDocs.objects.all()
       serializer = EmployeeDocsSerializer(employeedocs, many=True)
       return Response(serializer.data)

class EducationList(APIView):
    """
    A view for viewing List of Education
    """
    def get(self,request, format=None):
        
       education = Education.objects.all()
       serializer = EducationSerializer(education, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = EducationSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationDetail(APIView):
    """
    Retrieve, update or delete a education instance.
    """
    def get_object(self, pk):
        try:
            return Education.objects.get(pk=pk)
        except Education.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Education
        """
        education = self.get_object(pk)
        serializer = EducationSerializer(education)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        education = self.get_object(pk)
        serializer = EducationSerializer(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        education = self.get_object(pk)
        education.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)

class EducationDocsView(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

           document = EducationDocs.objects.filter(id=pk)
           serializer = EducationDocsSerializer(document, many=True)
           return Response(serializer.data)

    def post(self, request, pk=None):
        education = Education.objects.get(id=pk)
        request.data["education"]= education.id
        print(pk)
        print(request.data)
        serializer = EducationDocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
            try:
              return EducationDocs.objects.get(pk=pk)
            except EducationDocs.DoesNotExist:
             raise Http404

    def put(self, request, pk, format=None):
            
        education = Education.objects.get(id=pk)
        request.data["education"]= education.id
        educationdocs = self.get_object(pk)
        serializer = EducationDocsSerializer(educationdocs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)


class EducationdocsList(APIView):
    """
    A view for viewing List of Educationdocs
    """
    def get(self,request, format=None):
        
       educationdocs = EducationDocs.objects.all()
       serializer = EducationDocsSerializer(educationdocs, many=True)
       return Response(serializer.data)

class InternList(APIView):
    """
    A view for viewing List of Interns
    """
    def get(self,request, format=None):
        
       intern = Internship.objects.all()
       serializer = InternshipSerializer(intern, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = InternshipSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InternDetail(APIView):
    """
    Retrieve, update or delete a intern instance.
    """
    def get_object(self, pk):
        try:
            return Internship.objects.get(pk=pk)
        except Internship.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Intern
        """
        intern = self.get_object(pk)
        serializer = InternshipSerializer(intern)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
            
        # user = User.objects.get(id=pk)
        # request.data["user"]= user.id
        intern = self.get_object(pk)
        serializer = InternshipSerializer(intern, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        intern = self.get_object(pk)
        intern.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)