from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from slugify import slugify

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username} Daha önce login olmuşsun :/')
        return redirect('home_view')
    context = dict()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(username) < 6 or len(password) < 6:
            messages.warning(
                request, 'Lütfen kullanıcı adı ve şifre 6 karakterden büyük olması gerekmektedir')
            return redirect("user_profile:login_view")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Login oldun :)')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)


def register_view(request):
    if request.method == "POST":
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        instagram = post_info.get('instagram')

        if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or len(password) < 3:
            messages.warning(request, "Bilgiler en az 3 karakterden oluşmalıdır.")
            return redirect("user_profile:register_view")
        if email != email_confirm:
            messages.warning(request, "Lütfen Email bilgilerinizi kontrol ediniz")
            return redirect("user_profile:register_view")
        if password != password_confirm:    
            messages.warning(request, "Lütfen şifre bilgilerinizi kontrol ediniz")
            return redirect("user_profile:register_view")
        
        user, created = User.objects.get_or_create(username=email)
        if not created:
            user_login = authenticate(request, username=email, password=password)
            if user_login is not None:
                login(request, user_login)
                messages.info(request, f' Kayıtlı olmanızdan ötürü ana sayfaya yönlendirildiniz...')
                return redirect('home_view')
            else:
                messages.info(request, f'{email} adresi sistemde kayıtlı ama giriş yapamadınız... Login sayfasına yönlendirildiniz')
                return redirect('user_profile:login_view')
        # User models'de olan önce gönderilmelidirki OneToOne ilişkisi bozulmasın
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        profile, profile_created = Profile.objects.get_or_create(user=user)
        # Oluşturulan User'dan sonra Profle içine atılır ve kayıt gerçekleştirilir
        profile.instagram = instagram
        profile.slug = slugify(f"{ first_name } - { last_name }")
        user.save()
        profile.save()
        
        messages.success(request, f'{user.first_name} Başarıyla kayıt oldunuz ve Ana sayfaya yönlendirildiniz.')
        user_login = authenticate(request, username=email, password=password)
        login(request, user_login)
        return redirect('home_view')
    
    context = dict()
    return render(request, 'user_profile/register.html', context)


def logout_view(request):
    messages.success(
        request, f'{request.user.username} Başarıyla çıkış yaptınız')
    logout(request)
    return redirect('home_view')
