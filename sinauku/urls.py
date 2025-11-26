from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # halaman utama → index
    path('', include('akun.urls')), 
    path('mentor/', include('mentor.urls')),   
    path('orang_tua/', include('mentor.urls')),  
    path('peserta/', include('peserta.urls')), 
]
