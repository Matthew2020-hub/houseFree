from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render
from .serializers import UserSerializer
from .models import CustomUser
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# api/views.py
from rest_framework import generics


class ListTodo(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        return self.create(request)

# class CreateListAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     serializer_class = UserSerializer
  
#     lookup_field = 'user_id'
#     authentication_classes = [TokenAuthentication]
#     permisssion_classes = [IsAuthenticated]

    # def get(self, request, user_id, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def post(self, request):
    #     return self.create(request)

class CreateUpdateDestroyAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'user_id'
    authentication_classes = [TokenAuthentication]
    permisssion_classes = [IsAuthenticated]

    def get1(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, user_id):
        query = CustomUser.objects.filter(user_id=user_id)
        if query:
            return self.update(request)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, user_id):
        query = CustomUser.objects.get(apartment_id=user_id)
        if query:
            return self.destroy(request)
    

