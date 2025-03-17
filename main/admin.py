from django.contrib import admin
from .models import Blog, Project

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("created_at",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)