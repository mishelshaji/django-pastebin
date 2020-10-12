from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="user_home"),
    path('newpost/', new_post, name="user_new_post"),
    path('deletepost/<int:id>/', delete_post, name="user_delete_post"),
    path('editpost/<int:id>/', edit_post, name="user_edit_post"),
]