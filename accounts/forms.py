from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class LoginForm(AuthenticationForm):
    """Form for user login."""
    username = forms.CharField(
        max_length=100,
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': '100',
                'id': 'inputUsername',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'size': '100',
                'id': 'inputPassword',
                'placeholder': 'Password'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password']