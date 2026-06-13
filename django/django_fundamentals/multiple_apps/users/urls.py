from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('new', views.register, name='new_user'),
    path('login', views.login, name='login'),
    path('', views.get_all_users, name='get_all_users'),
]