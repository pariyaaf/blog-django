from django.shortcuts import render, get_object_or_404
from posts.models import PostModel
from .models import LikeModel
from django.http import JsonResponse


def like_post(request, post_id):
    pass
    post = get_object_or_404(PostModel, id=post_id)
    ip_address = request.META['REMOTE_ADDR']
    like, created = LikeModel.objects.get_or_create(post=post, ip_address=ip_address)
    
    if not created:
        like.delete()
        post.like = post.likes_count - 1
        post.save()
        liked = False
    else:
        post.like = post.likes_count + 1
        post.save
        liked = True

    return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})
