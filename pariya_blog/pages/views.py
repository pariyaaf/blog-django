from django.shortcuts import render
from django.http import HttpResponse
from posts.models import PostModel



def index(request):
    posts = PostModel.objects.order_by('-created_at').filter(is_published=True)[:6]
    return render (request, 'pages/index.html', {'posts' : posts})


def about(request):
    return render (request, 'pages/about.html')