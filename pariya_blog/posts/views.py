from django.shortcuts import render, get_object_or_404
from .models import PostModel
from django.core.paginator import Paginator


def index(request):
    posts = PostModel.objects.order_by('-created_at').filter(is_published=True)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_posts_list = paginator.get_page(page)
    context = {
        'posts':paged_posts_list
    }
    return render (request, 'posts/posts.html', context)


def post(request, post_id):
    post = get_object_or_404(PostModel.objects.filter(is_published=True), pk=post_id)
    return render(request, 'posts/post.html',{'post' : post})


def search(request):
    return render(request, 'posts/posts.html')