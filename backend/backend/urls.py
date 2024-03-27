from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/', include('apps.urls')),
    path('list/', include('apps.listu'))
]
