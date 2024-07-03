from django.shortcuts import render, get_object_or_404
from .models import PostModel
from django.core.paginator import Paginator
from django.db.models import Q
from comments.forms import CommentForm
from comments.models import CommentModel



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
    form = CommentForm()
    comments = CommentModel.objects.order_by('-comment_date').filter(is_published=True, post_id=post_id, parent=None)
    context = {
        'post':post,
        'form':form,
        'comments':comments
    }

    return render(request, 'posts/post.html', context)


def search(request):
    posts = PostModel.objects.order_by('-created_at').filter(is_published=True)
    
    # check if user search something
    if 'search_text' in request.GET:
        search_text = request.GET['search_text']

    if search_text:
        posts = posts.filter(Q(title__icontains=search_text)
                            | Q(text__icontains=search_text)
                            | Q(blogger__name__icontains=search_text))

    context = {
        'posts' : posts
    }
                            
        
    return render(request, 'posts/posts.html', context)