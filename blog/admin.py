from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'date_added', 'author', 'image')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')


admin.site.register(Comment)
admin.site.register(Post)
