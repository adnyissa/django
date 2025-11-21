from django.contrib import admin
from django.urls import path
from guru.views import index, edu, version1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guru/', index),
    path('edu/', edu),
    path('', index), 
    path('version1/', version1, name='version1')
]
