from django.urls import path
from . import views


app_name = 'editor'

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('notebooks/', views.notebooks_list, name='notebooks_list'),
    path('notebook/<slug:notebook_slug>/', views.notebook_content, name='notebook_content'),
]
