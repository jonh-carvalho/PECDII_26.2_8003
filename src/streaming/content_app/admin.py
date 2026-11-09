from django.contrib import admin

from content_app.models import Comment, Content, Like, Playlist


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'upload_date', 'views')
    list_filter = ('content_type', 'is_public')
    search_fields = ('title', 'description')
    ordering = ['-upload_date']  # Order by upload_date descending

    fieldsets = (
    ('Informações Básicas', {'fields': ('title', 'description')}),
    ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
    ('Detalhes Social', {'fields': ('likes', 'views')}),
  )

admin.site.register(Content, ContentAdmin)





admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Playlist)