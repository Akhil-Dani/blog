from django.contrib import admin
from . models import Profile, Post, Comment

# Register your models here.
@admin.register(Profile)
class ProfielAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio', 'image']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id' ,'author', 'title' ,'content', 'created_at']

@admin.register(Comment)    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post' ,'author', 'text']