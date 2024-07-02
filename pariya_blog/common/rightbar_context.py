from posts.models import PostModel

def rightbar_context(request):
    posts = PostModel.objects.order_by('-created_at').filter(is_published=True)[:6]
    return {
        'rightbar_context': posts,
    }