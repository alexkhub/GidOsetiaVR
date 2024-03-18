
from django.urls import path

from .views import *

urlpatterns = [
    path('registration/',  User_RegistrationCreateView.as_view() , name = 'registration'),
]