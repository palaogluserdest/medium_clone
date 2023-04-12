from django import forms

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("Ooops... En az 3 karakter olmalıdır :P")