from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list_view, name='post-list'),
    path('posts/following/', views.post_list_view, name='post-following'),  # Можно добавить логику для фильтрации
    path('posts/followers/', views.post_list_view, name='post-followers'),
    path('post-edit/<int:pk>/', views.post_update_view, name='post-edit'),
    path('post/<int:pk>/', views.post_detail_view, name='post-detail'),
    path('post-delete/<int:pk>/', views.post_delete_view, name='post-delete'),
    path('create-post/', views.post_create_view, name='create-post'),
    path('comment/<int:pk>/edit', views.comment_update_view, name='comment-edit'),
    path('comment/<int:pk>/delete', views.comment_delete_view, name='comment-delete'),
    path('post/<int:pk>/comment', views.comment_create_view, name='comment-create'),
]
