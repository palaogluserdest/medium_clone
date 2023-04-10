from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'instagram',
        'slug',
    ]


admin.site.register(Profile, ProfileAdmin,)
