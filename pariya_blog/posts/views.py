from django.shortcuts import render
from .models import PostModel
from django.core.paginator import Paginator
def index(request):
    posts = PostModel.objects.all()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_posts_list = paginator.get_page(page)

    context = {
        'posts':paged_posts_list
    }

    return render (request, 'posts/posts.html', context)

def post(request, post_id):
    return render(request, 'posts/post.html')

def search(request):
    return render(request, 'posts/posts.html')