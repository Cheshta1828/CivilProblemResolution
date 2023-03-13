from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import problems
#create problem form lfor adding problems to the databse from the user side 
class problemform(ModelForm):
    class Meta:
        model=problems
        fields="__all__"

