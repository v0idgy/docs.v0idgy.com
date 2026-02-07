from django.contrib import admin
from .models import Section, Page


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "slug", "order", "updated_at")
    list_filter = ("section",)
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "content_html")
    ordering = ("section", "order")
