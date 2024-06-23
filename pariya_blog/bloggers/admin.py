from django.contrib import admin

from .models import BloggerModel

class BloggerAdmin(admin.ModelAdmin):
    # display fields in admin panel
    list_display = ['id', 'name', 'email', 'birth_date', 'phone', 'created_at']

    # clickable fields
    list_display_links = ['id', 'name', 'email']

    # list_editable fields
    list_editable = ['birth_date']

    #list filter columns
    list_filter = ['name']

    #list searchable fileds
    search_fields = ['name', 'email', 'id', 'phone']

    # item in age pages
    list_per_page = 10

    # not editable
    readonly_fields = ['post_count', 'updated_by', 'deleted_by', 'deleted_at']


admin.site.register(BloggerModel, BloggerAdmin)