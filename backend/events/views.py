from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from django.db.models import Prefetch

from expeditions.models import Img


class EventListView(ListAPIView):
    queryset = Event.objects.all().prefetch_related(
        Prefetch('imgs', queryset=Img.objects.filter(first_img=True).only('img', 'first_img'))
    ).only('id', 'imgs', 'name', 'date_time', 'description', 'slug')
    serializer_class = EventSerializer


class EventDetailRetrieveView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'slug'
