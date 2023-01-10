from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital_index, name='hospitals'),
    path('add-hospital', views.hospital_create, name='hospital.create'),
    path('edit-hospital/<int:id>', views.hospital_edit, name='hospital.edit'),
    path('update-hospital/', views.hospital_update, name='hospital.update'),
    path('delete-hospital<int:id>', views.hospital_delete, name='hospital.delete'),

    # categories
    path('add-category', views.category_create, name='category.create'),

]