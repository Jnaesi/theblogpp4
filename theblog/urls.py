from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home, name="home"), <--> using class based views instead.
    path('', views.home, name="home"),
]