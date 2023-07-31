from django.contrib import admin
from django.urls import path
from .views import PlaceTable,update_place


urlpatterns = [

    path('first/',PlaceTable,name = 'first'),
    path('update/<int:pk>/',update_place,name = 'update')


]