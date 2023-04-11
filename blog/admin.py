from django.contrib import admin
from .models import BlogPost, Category, Tag


class BlogPostAdmin(admin.ModelAdmin):
   pass


class CategoryAdmin(admin.ModelAdmin):
   pass


class TagAdmin(admin.ModelAdmin):
   pass

admin.site.register(BlogPost, BlogPostAdmin,)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)