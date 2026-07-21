from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_coffe,name='all_coffe'),
    path('mocca/',views.mocca,name='mocca'),
]
