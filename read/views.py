from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost
from user_profile.models import Profile

def all_posts_view(request, user_slug):
    profile = get_object_or_404(Profile, slug=user_slug)
    posts = BlogPost.objects.filter(is_active=True, user=profile.user)
    context = dict(
        posts = posts,
        profile = profile,
    )
    return render(request, 'read/all_posts.html', context)
