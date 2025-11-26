from django.urls import path
from . import views

urlpatterns = [
    path('', views.peserta_dashboard, name='peserta_dashboard'),
]