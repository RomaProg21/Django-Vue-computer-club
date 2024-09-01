from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'Логин'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].label = ''













class RegisterUserForm(forms.ModelForm):
    password2 = forms.CharField(help_text=None,label='',widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }))
    class Meta:
        model = User
        fields = ['username','password']
        help_texts = {
            'username': None,
            'password': None,
            'pasword2': None,
        }
        labels = {
            'username': '',
            "password": '',
            "password2": '',
        }
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }
    def clean(self):
         cleaned_data = super(RegisterUserForm, self).clean()
         password = cleaned_data.get("password")
         confirm_password = cleaned_data.get("password2")

         if password != confirm_password:
              raise forms.ValidationError("Пароли не совпадают")
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user



