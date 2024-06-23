from django.contrib import admin


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
    readonly_fields = ['comments_count', 'likes_count', 'created_at', 'updated_by', 'deleted_by', 'deleted_at']
    date_hierarchy = 'created_at'
    list_select_related = ['blogger']


admin.site.register(PostModel, PostAdmin)