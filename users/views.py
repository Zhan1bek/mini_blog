from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Follow
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile', pk=user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/profile.html', {'user': user})

@login_required
def follow(request, pk):
    user_to_follow = get_object_or_404(User, pk=pk)
    Follow.objects.create(follower=request.user, following=user_to_follow)
    return redirect('profile', pk=pk)

@login_required
def unfollow(request, pk):
    user_to_unfollow = get_object_or_404(User, pk=pk)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile', pk=pk)
