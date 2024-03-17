from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', User_RegistrationCreateView.as_view(), name='registration'),
    path('create_comment/', CommentCreateView.as_view(), name='create_comment')
]
