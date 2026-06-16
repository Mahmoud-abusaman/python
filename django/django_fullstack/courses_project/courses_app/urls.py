from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/create', views.create, name='create'),
    path('courses/destroy/<int:id>', views.destroy, name='destroy'),
    path('courses/delete/<int:id>', views.delete, name='delete'),
    path('courses/<int:id>/comments', views.comments, name='comments'),
]
