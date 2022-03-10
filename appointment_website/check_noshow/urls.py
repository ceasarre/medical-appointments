from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='check-home'),
    path('add_person', views.add_person, name='check-add_person'),
    ]
