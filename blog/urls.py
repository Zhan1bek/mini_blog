from django.urls import path
from .views import (
    post_list,
    post_detail,
    post_create,
    post_edit,
    post_delete
)

urlpatterns = [
    path('', post_list, name='post_list'),  # Главная страница со списком постов
    path('post/<int:pk>/', post_detail, name='post_detail'),  # Страница детального просмотра поста
    path('post/new/', post_create, name='create_post'),  # Страница создания нового поста
    path('post/<int:pk>/edit/', post_edit, name='edit_post'),  # Страница редактирования поста
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),  # Страница удаления поста
]
