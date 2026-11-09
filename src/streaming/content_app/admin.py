from django.contrib import admin

from content_app.models import Comment, Content, Like, Playlist

# Register your models here.
admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Playlist)