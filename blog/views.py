from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogPostModelForm
from .models import Category, Tag, BlogPost
import json


@login_required(login_url='user_profile:login_view')
def create_blog_post_view(request):
    title = 'Yeni Blog Post'
    form = BlogPostModelForm()
    if request.method == "POST":
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # commit=False demeke hemen kaydetme değişiklik yapacam
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            tags = json.loads(form.cleaned_data.get('tag')) # bu şekilde yapıyı str formatından çıkardık
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value').lower())
                f.tag.add(tag_item)
            messages.success(request, 'Blog postunuz başarıyla kayıt edildi...')
            return redirect('home_view')
        else:
            messages.info(request, 'Hata dolayısıyla blog postunuzun kaydı gerçekleştirelemedi.')
    context = dict(
        form=form,
        title=title,
    )
    return render(request, 'common_components/form.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = BlogPost.objects.filter(category=category)
    context = dict(
        category = category,
        posts=posts,
    )
    return render(request, 'read/all_posts.html', context)

def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = BlogPost.objects.filter(tag=tag)
    context = dict(
        tag = tag,
        posts=posts,
    )
    return render(request, 'read/all_posts.html', context)