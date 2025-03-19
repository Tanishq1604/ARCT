from django.urls import path
from Backend2.views import GenerateHouseMapView

urlpatterns = [
    path('generate-house-map/',GenerateHouseMapView.as_view()),
]