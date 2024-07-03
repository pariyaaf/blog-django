from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from posts.models import PostModel
from django.http import JsonResponse
from .forms import CommentForm
from django.contrib import messages
from .models import CommentModel

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.user_name = request.user.username
                comment.user_email = request.user.email
                # handle parent comment
                if 'parent_id' in request.POST:
                    parent_id = int(request.POST.get('parent_id'))
                    comment.parent = CommentModel.objects.get(id=parent_id)

                comment.save()
                messages.success(request, 'نظر شما با موفقیت ثبت شد.')
                return JsonResponse({'success': True, 'message': 'کامنت با موفقیت ثبت شد.'})
            else:
                messages.error(request, 'برای ارسال کامنت باید وارد حساب کاربری خود شوید.')
                return JsonResponse({'success': False, 'errors': 'user not autherization'})
        else:
            messages.error(request, 'مشکلی در اطلاعات وارد شده وجود دارد.')
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'message': 'روش درخواست غیر معتبر است.'})