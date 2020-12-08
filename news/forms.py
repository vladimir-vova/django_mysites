from django import forms
from .models import News #Category
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',help_text='Пароль должен состоять из 150 символов', widget=forms.TextInput(
    attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
    attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
    attrs={"class": "form-control"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
    attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title','content','is_published','category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }
        
    #def clean_title(self):
    #    title = self.cleaned_data['title']
    #    if re.match(r'\d',title):
    #        raise ValidationError('Название начинается с цифры')





    #title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(
    #attrs={"class": "form-control"}))
    #content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(
    #attrs={"class": "form-control", "rows" : 5}))
    #is_published = forms.BooleanField(label='Опубликовано')
    #category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Category.objects.all(),label='Категория', widget=forms.Select(
    #attrs={"class": "form-control"}))