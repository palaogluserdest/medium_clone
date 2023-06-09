
from django.urls import path
from user_profile.views import (
    login_view,
    logout_view,
    register_view,
    profile_edit_view,
)

app_name = 'user_profile'

urlpatterns = [
    #Log in:
    path('login/', login_view, name='login_view'),
    # Register:
    path('register/', register_view, name='register_view'),
    #Log out:
    path('logout/', logout_view, name='logout_view'),
    #Profile Edit:
    path('profile/edit/', profile_edit_view, name='profile_edit_view'),

]
