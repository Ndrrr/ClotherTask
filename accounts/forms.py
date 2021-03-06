from django import forms  
from django.contrib.auth.forms import UserCreationForm,UserChangeForm  
from django.core.exceptions import ValidationError  
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=3, max_length=150)  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    
    class Meta:
        model = CustomUser
        fields = ['username']
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = CustomUser.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = CustomUser.objects.create_user(  
            self.cleaned_data['username'],  
        )  
        user.set_password(self.cleaned_data['password1'])
        print(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user  

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username']