from django.urls import path
from . import views

urlpatterns = [
    path('', views.members),
    path('reset', views.reset),
]