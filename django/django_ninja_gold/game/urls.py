
from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('process_money', views.process_money, name='process_money'),
]