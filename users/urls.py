from django.urls import path
from .views import (
    register,
    profile_view,
    profile_edit,
    follow_user,
    unfollow_user
)

urlpatterns = [
    path('register/', register, name='register'),  # Регистрация
    path('profile/<str:username>/', profile_view, name='profile_view'),  # Просмотр профиля
    path('profile/edit/', profile_edit, name='profile_edit'),  # Редактирование профиля
    path('follow/<str:username>/', follow_user, name='follow_user'),  # Подписаться на пользователя
    path('unfollow/<str:username>/', unfollow_user, name='unfollow_user'),  # Отписаться от пользователя
]