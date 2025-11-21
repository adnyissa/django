from django.contrib import admin
from django.urls import path
from guru.views import index, edu, version1, version2, version3, version4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guru/', index),
    path('edu/', edu),
    path('', index), 
    path('version1/', version1, name='version1'),
    path('version2/', version2, name='version2'),
    path('version3/', version3, name='version3'),
    path('version4/', version4, name='version4'),

]
