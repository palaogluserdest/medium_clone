
from django.urls import path
from .views import all_posts_view

app_name = 'read'

urlpatterns = [
    # Kullanıcı yazıları
    path('<slug:user_slug>/',all_posts_view , name='all_posts_view'),

]
