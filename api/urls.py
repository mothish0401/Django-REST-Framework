from home.views import university
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('university/', university),
]