from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo/new', views.add_dojo),
    path('ninja/new', views.add_ninja),
    path('dojo/<int:dojo_id>/delete', views.delete_dojo),
]