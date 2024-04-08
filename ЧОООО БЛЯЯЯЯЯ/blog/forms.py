from django import forms
from .models import Article, CustomUser, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content','photo','publish','category')

        widgets = {
            'title':forms.TextInput(attrs={'class':"form-control",'placeholder':"Title"}),
            'content':forms.Textarea(attrs={'class':"form-control",'placeholder':"Write a content"}),
            'photo':forms.FileInput(attrs={'class':"form-control"}),
            'publish':forms.CheckboxInput(attrs={'class':"form-check-input"}),
            'category':forms.Select(attrs={'class':"form-select"}),
        }

class UserRegister(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"User Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"********"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"********"}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"User Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"********"}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title',)
        widgets = {
            'title':forms.Textarea(attrs={
                'class':"form-control",
                'placeholder':"Write your comment"
            })
        }