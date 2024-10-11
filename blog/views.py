from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, render, redirect, get_object_or_404
from django.db.models import Q

from .forms import PostForm, CommentForm, SearchForm
from .models import Post, Comment


# Главная страница
def index(request):
    return render(request, 'main-page/index.html')


# Список постов
def post_list_view(request):
    search_value = request.GET.get('search', None)
    posts = Post.objects.all()

    if search_value:
        query = Q(title__icontains=search_value)
        posts = posts.filter(query)

    search_form = SearchForm(request.GET)
    context = {'posts': posts, 'search_form': search_form}
    return render(request, 'main-page/post/posts.html', context)


# Детали поста
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'main-page/post/post-detail.html', context)


# Создание поста
@login_required
def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'main-page/post/create_post.html', {'form': form})


# Обновление поста
@login_required
def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return redirect('login')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'main-page/post/update-post.html', {'form': form})


# Удаление поста
@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.author:
        post.delete()
        return redirect('post-list')
    return redirect('post-detail', pk=post.pk)


# Создание комментария
@login_required
def comment_create_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)

    return render(request, 'main-page/comment/create.html', {'form': CommentForm(), 'post': post})


# Удаление комментария
@login_required
def comment_delete_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user == comment.author:
        comment.delete()

    return redirect('post-list')


# Обновление комментария
@login_required
def comment_update_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        return redirect('login')

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-list')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'main-page/comment/edit.html', {'form': form})
