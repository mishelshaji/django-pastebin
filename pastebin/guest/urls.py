from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="homepage"),
    path('about/', about, name="aboutpage"),
    path('login/', user_login, name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', register, name="register"),
    path('search/', search, name="search"),
]