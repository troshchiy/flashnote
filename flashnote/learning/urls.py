from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'learning'

urlpatterns = [
    path('page/<uuid:page_id>/', login_required(views.LearnView.as_view()), name='learn')
]
