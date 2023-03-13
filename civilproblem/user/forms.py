from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import myuser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class myuserform(UserCreationForm):
    adhaar=forms.CharField(max_length=19)
    city=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    address=forms.CharField(max_length=2000)
    contact=forms.CharField(max_length=10)
     
    class Meta:
        model=User
        fields=('username','email','city','adhaar','address','contact','password1','password2')
 
