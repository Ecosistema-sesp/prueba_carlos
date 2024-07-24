# myapp/urls.py
from django.urls import path
from .views import login_view, success_view, home

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('success/', success_view, name='success'),

]
