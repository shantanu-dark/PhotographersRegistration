# photographer_app/urls.py
from django.urls import path
from .views import add_photographer, search_photographer, show_all_photographers

urlpatterns = [
    path('add/', add_photographer, name='add_photographer'),
    path('search/', search_photographer, name='search_photographer'),
    path('show_all/', show_all_photographers, name='show_all_photographers'),
]
