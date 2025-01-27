from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('collaborate_success/', views.collaborate_success, name='collaborate_success'),
]