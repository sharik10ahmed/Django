from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    full_name = forms.CharField(max_length=200)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email']