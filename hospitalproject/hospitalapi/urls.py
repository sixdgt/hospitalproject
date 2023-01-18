from django.urls import path
from .views import HospitalApiView

urlpatterns = [
    path('hospital/', HospitalApiView.as_view())
]