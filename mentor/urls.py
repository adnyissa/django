from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor_dashboard, name='mentor_dashboard'),
]
