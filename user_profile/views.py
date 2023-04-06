from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .models import User


def login_view(request):
    # login olan kullanıcı direkt olarak ana sayfaya yönlendirilsin.
    # u = User.objects.get(username='farklyzz')
    # u.set_password('47721.GsP')
    # u.save()
    context = dict()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)
