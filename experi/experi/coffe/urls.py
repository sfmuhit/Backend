from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_coffe,name='all_coffe'),
    path('<int:coffe_id>/',views.coffe_details,name='coffe_details'),
]
