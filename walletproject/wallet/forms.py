from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Wallet

class UserSignup(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))

    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter confirmed password'}))

    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email','first_name': "First Name",'last_name':'Last Name'}
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                 'placeholder': 'enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
               'placeholder': 'enter last name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter email'
            }),
        }


class UserLogin(AuthenticationForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))          
    class Meta:
        model=User
        fields=['username']
       
    
# class ToDoForm(forms.ModelForm):
#     class Meta:
#         model = TODO
#         fields = ['title','status','priority']
#         widgets={
#             'title':forms.TextInput(attrs={'class':'form-control'}),
#             'status':forms.Select(attrs={'class':'form-control'}),
#             'priority':forms.Select(attrs={'class':'form-control'}),
#         }

