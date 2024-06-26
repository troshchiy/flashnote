from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'learning'

urlpatterns = [
    path('<str:notebook_or_page>/<uuid:notebook_or_page_id>/', login_required(views.LearnView.as_view()), name='learn')
]
