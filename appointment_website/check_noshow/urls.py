from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='check-home'),
    path('add_person/', views.add_person, name='check-add_person'),
    path('history/', views.history, name='check-history'),
    path('results/', views.results, name='check-results'),
    ]
