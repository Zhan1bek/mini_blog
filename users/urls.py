from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/follow/', views.follow, name='follow'),
    path('profile/<int:pk>/unfollow/', views.unfollow, name='unfollow'),
]
