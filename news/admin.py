from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at")
    list_filter = ("published_at", "author")
    search_fields = ("title", "content")