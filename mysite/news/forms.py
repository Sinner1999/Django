from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs = {"class": "form-control"}),
            'content': forms.Textarea(attrs = {"class": "form-control"}),
            'is_published': forms.CheckboxInput(attrs = {"class": "form-check-input", "role": "switch"}),
            'category': forms.Select(attrs = {"class": "form-control"}),
        }
    
    # title = forms.CharField(max_length = 150, label = "Назвавние", widget = forms.TextInput(attrs = {"class": "form-control"}))
    # content = forms.CharField(label = "Текст", widget = forms.Textarea(attrs = {"class": "form-control"}))
    # is_published = forms.BooleanField(label = "Опубликовано", initial = True, widget = forms.CheckboxInput(attrs = {"class": "form-check-input", "role": "switch"}))
    # category = forms.ModelChoiceField(queryset = Category.objects.all(), label = "Категория", empty_label = 'Choose category...', widget = forms.Select(attrs = {"class": "form-control"}))
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title is not started by digit')
        return title
    
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs = {"class": "form-control"}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs = {"class": "form-control", "autocomplete": "off"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {"class": "form-control"}))
    password2 = forms.CharField(label='Retype Password', widget=forms.PasswordInput(attrs = {"class": "form-control"}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs = {"class": "form-control"}),
            'email': forms.EmailInput(attrs = {"class": "form-control"}),
            'password1': forms.PasswordInput(attrs = {"class": "form-control", "type": "password"}),
            'password2': forms.PasswordInput(attrs = {"class": "form-control", "type": "password"}),
            
        }
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs = {"class": "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {"class": "form-control"}))