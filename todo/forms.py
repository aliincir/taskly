from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Task

from django import forms



class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']        



class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))  # Default TextInput widget
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))  # Use PasswordInput directly

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

# --- Create a Task

class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Task
        fields = ['title', 'content',]
        exclude = ['user', ]