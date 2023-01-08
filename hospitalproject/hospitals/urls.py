from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital_index, name='hospitals'),
    path('add-hospital', views.hospital_create, name='hospital.create'),

    # categories
    path('add-category', views.category_create, name='category.create'),

]