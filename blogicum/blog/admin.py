from django.contrib import admin

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("category_id",)
    list_display = ("text", "pub_date", "author", "location", "category")


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)
