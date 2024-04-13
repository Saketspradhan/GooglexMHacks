from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('routes', views.routes, name='routes'),
    path('survey/', views.survey_view, name='survey'),
    path('itinerary/', views.generate_itinerary, name='generate_itinerary'),

]