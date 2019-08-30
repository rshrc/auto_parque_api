from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zone/', include('zone.urls')),
    path('entry_log/', include('entry_log.urls')),
]
