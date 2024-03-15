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
