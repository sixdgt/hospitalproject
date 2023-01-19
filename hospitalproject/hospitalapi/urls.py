from django.urls import path
from .views import HospitalApiView, HospitalApiIdView

urlpatterns = [
    path('hospital/', HospitalApiView.as_view()),
    path('hospital/<int:id>', HospitalApiIdView.as_view()),
]