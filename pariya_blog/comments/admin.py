from django.contrib import admin
from .models import CommentModel
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_email', 'post_id', 'is_published']

    ordering = ['comment_date']

    list_display_links = ['user_name', 'user_email']

    list_editable = ['is_published']

    list_filter = ['user_name', 'user_email', 'post_id']

    search_fields = ['comment_text', 'user_name', 'user_email', 'post_id', 'post__text']

    readonly_fields = ['comment_text', 'user_name', 'user_email', 'comment_date', 'post']




admin.site.register(CommentModel, CommentAdmin)