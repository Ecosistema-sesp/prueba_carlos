# prueba_unp/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Including myapp urls
    path('', home, name='home'),  # Fixing the home route
    path('', include('myapp.urls')),
]
