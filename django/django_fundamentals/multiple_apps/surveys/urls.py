

from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_all_surveys, name='get_all_surveys'),
    path('new', views.new_survey, name='new_survey'),
]