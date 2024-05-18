from django.urls import path
from . import views


app_name = 'editor'

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
]
