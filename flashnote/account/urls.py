from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
