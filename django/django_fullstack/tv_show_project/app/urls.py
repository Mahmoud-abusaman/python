
from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.add_new),
    path('shows/<int:id>', views.details),
    path('shows/<int:id>/edit', views.update),
    path('shows/<int:id>/delete', views.delete),
]