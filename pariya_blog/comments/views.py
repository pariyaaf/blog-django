from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from posts.models import PostModel
from django.http import JsonResponse
from .forms import CommentForm


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return JsonResponse({'success': True, 'message': 'کامنت با موفقیت ثبت شد.'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'روش درخواست غیر معتبر است.'})