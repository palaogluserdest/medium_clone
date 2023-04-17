from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from slugify import slugify
from blog.models import BlogPost
from .forms import ProfileModelForm


@login_required(login_url='user:login_view')
def profile_edit_view(request):
    user = request.user
    initial_data = dict(
        first_name = user.first_name,
        last_name = user.last_name,
    )
    form = ProfileModelForm(instance=user.profile, initial=initial_data)
    if request.method == 'POST':
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=user.profile)
        if form.is_valid():
            f = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            f.save()
            messages.success(request, 'Profiliniz güncellendi...')
            return redirect('user_profile:profile_edit_view')

    title = 'Profili Düzenle'
    context = dict(
        form=form,
        title=title,
    )
    return render(request, 'common_components/form.html', context)



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


