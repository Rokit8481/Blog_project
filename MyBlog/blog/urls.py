from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post, name='post'),
    path('author/<int:author_id>/posts/', views.author, name='author')
]