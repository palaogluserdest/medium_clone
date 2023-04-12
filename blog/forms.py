from django import forms
from django.core import validators
from tinymce.widgets import TinyMCE
from .models import BlogPost
# Our Validators
from config.validators import min_length_3


# def min_length_3(value):
#     if len(value) < 3:
#         raise forms.ValidationError("Ooops... En az 3 karakter olmalıdır :P")


class BlogPostModelForm(forms.ModelForm):
   
    tag = forms.CharField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 20}))
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message=f'En az 3 karakter olmalıdır...')])
    title = forms.CharField(validators=[min_length_3, ]) # kendi oluşturgumuz validator çağrıldı
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'cover_image',
            'category',
            'tag',
        ]
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError("Title must be at least 3 characters long")
    #     return title.upper()