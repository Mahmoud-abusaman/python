
from . import views
from django.urls import path
urlpatterns = [
    path('', views.get_all_blogs, name='get_all_blogs'),
    path('<int:id>', views.get_blog_by_id, name='get_blog_by_id'),
    path('new', views.new_blog, name='new_blog'),
    path('<int:id>/edit', views.edit_blog, name='edit_blog'),
    path('<int:id>/delete', views.delete_blog, name='delete_blog'),
]