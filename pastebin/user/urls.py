from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="user_home"),
    path('newpost', new_post, name="user_new_post"),
]