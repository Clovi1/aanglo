from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tag', 'author', 'time_create', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ('id', 'tag', 'time_create')
    list_editable = ('is_published',)
    list_filter = ('tag', 'author', 'time_create', 'is_published')
    prepopulated_fields = {'slug': ('title',)}

    save_as = True
    save_on_top = True

    fields = (
        'author', 'title', 'slug', 'tag', 'content', 'image', 'get_html_image', 'is_published', 'time_create')
    readonly_fields = ('time_create', 'get_html_image')

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=50>')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website', 'time_create', 'post')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'email')

    fields = (
        'name', 'email', 'website', 'post', 'message', 'time_create')
    readonly_fields = ('time_create',)


@admin.register(UserEmails)
class UserEmailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('id', 'email')
    search_fields = ('id', 'email')


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_icon')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

    def get_html_icon(self, object):
        if object.icon:
            return mark_safe(f'<img src="{object.icon.url}" width=20>')


admin.site.site_title = 'AAnglo administration'
admin.site.site_header = 'AAnglo administration'
