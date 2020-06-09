from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from django.contrib import messages


def home(request):
    post = Posts.objects.all()
    context = {
        'post': post
    }
    return render(request, 'posts/home.html', context)


def post_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post_title = request.POST.get('post_title')
            post_content = request.POST.get('post_content')
            new = Posts(post_title=post_title, post_content=post_content, author=request.user)
            new.save()
            return redirect('home')
    else:
        messages.success(request, 'Login to access this page')
        return redirect('login')
    return render(request, 'posts/create_post.html')


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail_page.html', context)


def update_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    context = {
        'post': post
    }
    if request.user.is_authenticated and request.user == post.author:
        if request.method == 'POST':
            post.post_title = request.POST.get('post_title')
            post.post_content = request.POST.get('post_content')
            post.save()
            return redirect('home')
    else:
        messages.error(request, 'You dont have access to this page')
        return redirect('home')
    return render(request, 'posts/update_page.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    post.delete()
    return redirect('home')
