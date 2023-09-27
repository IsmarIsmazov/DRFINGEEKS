from django.contrib import admin

from app.models import Post, Category, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "descriptions", "created_at", "modifite_at", 'likes')
    list_display_links = ("likes",)
    search_fields = ("title", "descriptions")


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)

