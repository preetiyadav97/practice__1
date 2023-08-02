from django.contrib import admin
from django.urls import path
from .views import PlaceTable,update_place,view,Create_place,Delete_place


urlpatterns = [

    path('first/',PlaceTable,name = 'first1'),
    path('update/<int:pk>/',update_place,name = 'update1'),
    path('reate/',Create_place,name = 'reate1'),
    path('del/<int:pk>/',Delete_place,name = 'delete1'),


    path('show/<int:pk>/',view,name="vie")


]