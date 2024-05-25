from django.urls import path
from . import views


app_name = 'editor'

urlpatterns = [
    path('notebooks/', views.notebooks_list, name='notebooks_list'),
    path('notebook/<uuid:notebook_id>/', views.notebook_content, name='notebook_content'),
    path('page/<uuid:page_id>/', views.page_content, name='page_content'),
]
