from django.urls import path
from . import views

urlpatterns = [
    path('', views.ortu_dashboard, name='ortu_dashboard'),
]