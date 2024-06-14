from django import forms 
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name','email','body']
        # exclude = ['author']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']