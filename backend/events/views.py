from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import *
from .serializers import *
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from expeditions.models import Img, Comment
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status


class EventListView(ListAPIView):
    queryset = Event.objects.all().prefetch_related(
        Prefetch('imgs', queryset=Img.objects.filter(first_img=True).only('img', 'first_img'))
    ).only('id', 'imgs', 'name', 'date_time', 'description', 'slug')
    serializer_class = EventListSerializer


class EventDetailRetrieveView(RetrieveAPIView):
    queryset = Event.objects.all().prefetch_related(
        Prefetch('imgs', queryset=Img.objects.filter(first_img=True).only('img', )),
        Prefetch('comments',
                 queryset=Comment.objects.all().select_related('user').only('text', 'date', 'rating', 'user__username'))
    )
    serializer_class = EventSerializer
    lookup_field = 'slug'


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentEventSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, JWTAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
