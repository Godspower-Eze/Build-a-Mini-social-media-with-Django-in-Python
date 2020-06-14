from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']


class Login_Form(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


gender = (
    ('', ''),
    ('male', 'Male'),
    ('female', 'Female')
)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio_data', 'first_name', 'last_name', 'gender', 'picture']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
