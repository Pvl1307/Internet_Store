from django.contrib import admin

from weblog.models import WeBlog


@admin.register(WeBlog)
class WeBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'text', 'blog_img', 'date_of_creation', 'is_published')
