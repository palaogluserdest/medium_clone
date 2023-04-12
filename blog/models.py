from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Third Party App:
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class BaseModel(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         # Buradaki adlandırma path kısmında verilen name bilgisdir.
    #         'blog:category_view',
    #         kwargs={
    #             "category_slug": self.slug
    #         }
    #     )


class Tag(BaseModel):
   
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         'blog:tag_view',
    #         kwargs={
    #             "tag_slug": self.slug
    #         }
    #     )


class BlogPost(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag,)
    cover_image = models.ImageField(upload_to='post')
    count=models.PositiveBigIntegerField(default=0)
    

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #             'blog:post_detail_view',
    #         kwargs={
    #             "category_slug": self.category.slug,
    #             "post_slug": self.slug
    #         }
    #     )
