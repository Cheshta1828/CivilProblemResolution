from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
     return render(request, 'index.html')
# def userlogin(request):
#      return render(request,'userlogin.html')
# def adminlogin(request):
#      return render(request,'adminlogin.html')
# def register(request):
#      return render(request,'register.html')
def about(request):
     return render(request,'about.html')

