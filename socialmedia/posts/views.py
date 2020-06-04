from django.shortcuts import render, HttpResponseRedirect
from .models import Posts
from django.contrib.auth.models import User


def home(request):
    post = Posts.objects.all()
    context = {
        'post':post
    }
    return render(request, 'posts/home.html', context )


def post_create(request):
    if request.method == 'POST':
        post_title = request.POST.get('post_title')
        post_content = request.POST.get('post_content')
        new = Posts(post_title=post_content, post_content=post_content, author_id = 1  )
        new.save()
        return HttpResponseRedirect('/')
    return render(request, 'posts/create_post.html')