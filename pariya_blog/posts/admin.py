from django.contrib import admin
from bloggers.models import BloggerModel

from .models import PostModel

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'blogger', 'comments_count', 'likes_count', 'is_published', 'created_at']

    list_display_links = ['id', 'title']

    list_editable = ['is_published']

    list_filter = ['blogger']

    search_fields = ['title', 'blogger__name', 'text']

    list_per_page = 10

    # another 
    ordering = ['id']
    readonly_fields = ['comments_count', 'likes_count', 'created_at', 'updated_by', 'deleted_by', 'deleted_at', 'blogger']
    date_hierarchy = 'created_at'
    list_select_related = ['blogger']

    # static fields for anyusers
    def save_model(self, request, obj, form, change):
        if not obj.blogger:
            obj.blogger = BloggerModel.objects.filter(user=request.user).first()
        if obj.blogger is None:
            raise ValueError("The current user is not associated with any BloggerModel.")
        super().save_model(request, obj, form, change)


    # just show user posts
    def get_queryset(self, request):
        qs =  super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(blogger__user=request.user)


admin.site.register(PostModel, PostAdmin)