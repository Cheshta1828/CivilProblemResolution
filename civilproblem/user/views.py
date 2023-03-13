from ast import Not
from django.shortcuts import render,HttpResponse,redirect
from main.models import problems
from django.contrib.auth import authenticate,login,logout
#import authenticate

from django.contrib import messages
from main.forms import problemform
from user.forms import myuserform
from user.models import myuser
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def userlogin(request):
     if(request.method=='POST'):
          username=request.POST['username']
          password=request.POST['password']
          
          user=authenticate(request ,username=username,password=password)
          print(username)
          print(password)
          print(user)
          if user is not None:
               login(request,user)
               print("logged in successfully")
               return redirect('hello')
               
          else:
               print("failed")
     else:
          print("rendering userlogin again")
          return render(request, 'userlogin.html')

def searchproblem(request):
     if request.method=="POST":
          searched=request.POST['searched']
          problem=problems.objects.all()
          if problem:
               problem=problems.objects.filter(Q(title__icontains=searched))
          context={
            'problems':problem
          }

             
     return render(request,'userview.html',context)
def userlogout(request):
     logout(request)
     return redirect('/')


def register(request):
     if request.method == 'POST':
        form = myuserform(request.POST)
        print(form)
        username=request.POST['username']
        print(username)
        email=request.POST['email']
        print(email)
        password=request.POST['password2']
        adhaar=request.POST['adhaar']
        print(adhaar)
        city=request.POST['city']
        contact=request.POST['contact']
        address=request.POST['address']
        print(password)
        user1=User(username=username,password=password,email=email)
        new_my_user=myuser(user=user1,adhaar=adhaar,city=city,contact=contact,address=address,email=email)
        user1.save()
        print("saved the default user")
        new_my_user.save()
        print("saved the new user")
     else:
          form = myuserform()
          print("error!!! ")
          return render(request, 'register.html', {'form':form})
     return render(request, 'userlogin.html')


# def register(request):
#      if request.method == 'POST':
#           form = myuserform(request.POST)
#           if form.is_valid():
#                form.save()
#                return redirect('userlogin')
#      else:
#         if request.user.is_authenticated:
#             messages.info(request, 'Already have an account.')
#             return redirect('userlogin')

#         form = myuserform()
#      return render(request, 'register.html', {'form': form})

def hello(request):
     # myyuser=myuser.objects.get(user=request.user)

     # context={'myuser':myyuser}
     # # print(user)
     return render(request,'hello.html')


def userview(request):
     problem=problems.objects.all()
     context={
        'problems':problem
    }
    
     return render(request,'userview.html',context)

def useraddprob(request):
     submitted=False
     if request.method=='POST':
          form=problemform(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('useraddprob?submitted=True')
     else:
          form=problemform
          if 'submitted' in request.GET:
               submitted=True

          
     return render(request,'useraddprob.html',{'form':form ,'submitted':submitted})






def editprofile(request,id):
     print("hello")


     
     print(id)
     modify=myuser.objects.get(user=id)
     print(modify)
     form=myuserform(request.POST or None,instance=modify )
     print(form)
#      if form.is_valid():
#           form.save()
#           return redirect('/home')

#      users=myuser.objects.all()
#      context={
#         'users':users,
#         'form':form
#     }
#      return render(request,'editprofile.html',context)
     if request.method == 'POST':
        username=request.POST['username']
        print(username)
        email=request.POST['email']
        print(email)
        password=request.POST['password2']
        adhaar=request.POST['adhaar']
        print(adhaar)
        city=request.POST['city']
        contact=request.POST['contact']
        address=request.POST['address']
        print(password)
        user1=User(username=username,password=password,email=email)
        new_my_user=myuser(user=user1,adhaar=adhaar,city=city,contact=contact,address=address,email=email)
        user1.save()
        print("saved the default user")
        new_my_user.save()
        print("saved the new user")
        context={'form':form}
        return render (request,'editprofile.html',context)
     #return  render (request,'editprofile.html',context)
def vote(request,id=0):
     print(id)

     modify=problems.objects.get(prob_id=id)
     print("hello")
     print(modify)
     print(modify.votes)
     modify.votes+=1
     modify.save()
     print(modify.votes)
     
     problem=problems.objects.all()
     mycontext={
          'problems':problem
          }
     return render(request,'userview.html',mycontext)



     





