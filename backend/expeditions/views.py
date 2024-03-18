from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView, CreateAPIView
# Create your views here.
from .models import *
from .serializers import *


class User_RegistrationCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_RegistrationSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)