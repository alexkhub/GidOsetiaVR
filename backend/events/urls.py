from django.urls import path

from .views import *

urlpatterns = [
    path('events/',  EventListView.as_view(), name='events'),
    path('comment/<slug:slug>/', CommentCreateView.as_view(), name='comment'),
    path('event_detail/<slug:slug>/', EventDetailRetrieveView.as_view() , name='event_detail'),

]
