from django.urls import path
from . import views


app_name = 'editor'

urlpatterns = [
    path('', views.notes_questions_list, name='notes_questions_list'),
]
