from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital_index, name='hospitals'),
]