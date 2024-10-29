from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, PasswordInput, HiddenInput, FileInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=HiddenInput(attrs={'placeholder': 'username..', 'class': "form-control", 'style': 'max-width: 300px;'}), label='')
    email = forms.EmailField(widget=EmailInput(attrs={'placeholder': 'E-Mail..', 'class': "form-control", 'style': 'max-width: 300px;'}), label='')
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password..', 'class': "form-control", 'style': 'max-width: 300px;'}), label='')

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(max_length=8, label='', widget=PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }))
    password2 = forms.CharField(max_length=8,label='', widget=PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }))
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "age", "password1", "password2")
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'age': NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Age'
                })
        }
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "age": ""
        }

class CustomUserUpdateForm(ModelForm):
    avatar = forms.ImageField(required=False, widget=FileInput(attrs={'class': "form-control", 'style': 'max-width: 300px;'}), label='Avatar')
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", 'email', "age"]
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'age': NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Age'
                })
        }
        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "email": "E-mail:",
            "age": "Age:"
        }

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': "form-control mb-4 align-self-center", 
                'style': 'max-width: 300px;',
                'placeholder': 'Old Password:'
                }), label='')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': "form-control mb-4 align-self-center", 
                'style': 'max-width: 300px;',
                'placeholder': 'New Password:'
                }), label='')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': "form-control mb-4 align-self-center", 
                'style': 'max-width: 300px;',
                'placeholder': 'New Password again:'
                }), label='')