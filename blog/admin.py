from django.contrib import admin
from .models import BlogPost, Category, Tag


class BlogPostAdmin(admin.ModelAdmin):
   list_display=[
      'pk',
      'title',
      'slug',
      'is_active',
      'view_count',
   ]
   list_display_links=[
      'title'
   ]


class CategoryAdmin(admin.ModelAdmin):
    list_display=[
      'pk',
      'title',
      'slug',
   ]


class TagAdmin(admin.ModelAdmin):
    list_display=[
      'pk',
      'title',
      'slug',
   ]

admin.site.register(BlogPost, BlogPostAdmin,)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)