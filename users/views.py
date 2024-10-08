from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Импортируем модель User
from .models import Profile, Follow
from .forms import ProfileForm

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход после регистрации
            return redirect('post_list')  # Перенаправление на список постов
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})

# User Profile View
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    followers = profile.followers.all()
    following = profile.following.all()
    return render(request, 'users/profile.html', {
        'profile': profile,
        'followers': followers,
        'following': following,
    })

# Edit User Profile
@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # Указываем request.FILES
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile_edit.html', {'form': form})

# Follow a User
@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile_view', username=username)

# Unfollow a User
@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile_view', username=username)
