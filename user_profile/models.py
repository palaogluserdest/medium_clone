# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class UserManager(BaseUserManager):
#     # Burası User modelimiz için hesap oluşturma fonksiyonlarını yazacağımız kısım olacak.
#     def create_user(self, username, email, password, **kwargs):
#         # **kwargs varsa diğer tüm bölümleri tutmak için.
#         if not username:
#             raise ValueError('The given username must be set')
#         if not email:
#             raise ValueError('The given email must be set')
#         if not password:
#             raise ValueError('The given password must be set')
        
#         # Bu üst kısım if kontrolü ile değerleri kontrol ettik. Eğer eksik varsa create işlemi yapılmayacak.

#         user = self.model(
#             username = username,
#             email = email,
#             **kwargs
#         )
#         # Şu kısım bu fonksiyon çağrıldığında, çağıran model üzerinde create yaptırır.

#         user.set_password(password)
#         # set_password ile password'u şifreli olarak koyarız.
#         # field'larda password yazmadık modelde çünkü password varsayılan olarak AbstractBaseUser içerisinde mevcut.
#         #Şimdi de create_superuser yazalım
#         user.save()
#         return user
    
#     def create_superuser(self, username, email, password, **kwargs):
#         # Hiç kontrol yazmayacağım direkt üst fonksiyonu çalıştıracağım
#         user = self.create_user(username, email, password, **kwargs)
#         # ancak bu bir admin user olduğu için staff True yapmalıyız.
#         user.is_staff=True
#         user.save()

#         return user
# class User(AbstractBaseUser, PermissionsMixin):
#     # Kullanıcının username field
#     username = models.CharField(max_length=32, unique=True)
#     # Email tutacak field
#     email = models.EmailField(unique=True)
#     # Kullanıcının admin durumunu kontrol etme, bu zorunlu
#     is_staff = models.BooleanField(default=False)
#     # Hesabın aktif olup olmadığını kontrol etme
#     is_active = models.BooleanField(default=True)
#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self) -> str:
#         return self.email
