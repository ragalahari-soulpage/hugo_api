from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse,HttpResponse,Http404

from hugo.api.serializers import(
    UserSerializer, SalarySerializer, user)
from hugo.db.models import(
    User, Salary)


def get_tokens_for_user(user):

    refresh = RefreshToken.for_user(user)

    return {
       "refresh": str(refresh),
       "access": str(refresh.access_token),
   }
class UserListCreate(APIView):
    def post(self, request):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           user = serializer.save()
           user.set_password(request.data.get("password"))
           user.save()
           jwt_token = get_tokens_for_user(user)
           jwt_token["username"] = request.data.get("username")
           jwt_token["email"] = request.data.get("email")
           return JsonResponse(jwt_token, safe=False)


class UserDetail(APIView):
   def get(self, request):
       permission_classes = (IsAuthenticated,)
       user = request.user
       if user.id != None:
           serializer = UserSerializer(user)
           return Response(serializer.data)
       return Response(
           {"error": "Authentication credentials were not provided."},
           status=status.HTTP_401_UNAUTHORIZED,
       )


class SalaryList(APIView):
    """
    A view for viewing List of salary
    """
    def get(self,request, format=None):
        
       salary = Salary.objects.all()
       serializer = SalarySerializer(salary, many=True)
       return Response(serializer.data)

    
    def post(self, request):
         
         serializer = SalarySerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalaryDetail(APIView):
    """
    Retrieve, update or delete a salary instance.
    """
    def get_object(self, pk):
        try:
            return Salary.objects.get(pk=pk)
        except Salary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return salary
        """
        salary = self.get_object(pk)
        serializer = SalarySerializer(salary)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        user = User.objects.get(id=pk)
        request.data["user"]= user.id
        salary = self.get_object(pk)
        serializer = SalarySerializer(salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Deleted Successfully"} , serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        salary = self.get_object(pk)
        salary.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)