from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_page, name='auth'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]