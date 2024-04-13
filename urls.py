from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.survey_view, name='survey'),
    path('itinerary/', views.generate_itinerary, name='generate_itinerary'),
]