from django.shortcuts import HttpResponse, redirect, render

from .models import problems,feedback
from .forms import problemform
from django.http import HttpResponseRedirect
from user.models import myuser
from django.db.models import Q

# Create your views here.
def adminlogin(request):
     return render(request,'adminlogin.html')

def adminlogout(request):
     return redirect('/')
def notsolved(request):
     problem=problems.objects.all()
     context={
        'problems':problem
    }
    #print(context)
    #return render(request,'viewbooks.html',context)
     #return render(request,'view.html',context)
     return render(request,'ns.html',context)
def progress(request):
     problem=problems.objects.all()
     context={
        'problems':problem
    }
     return render(request,'ip.html',context)
def complete(request):
     problem=problems.objects.all()
     context={
        'problems':problem
    }
    #print(context)
    #return render(request,'viewbooks.html',context)
     #return render(request,'view.html',context)
     #return render(request,'ns.html',context)
     return render(request,'c.html',context)
def searchproblem(request):
     if request.method=="POST":
          searched=request.POST['searched']
          print(searched)
          problem=problems.objects.all()
          if problem:
               problem=problems.objects.filter(Q(title__icontains=searched))
          context={
            'problems':problem
          }

             
     return render(request,'main/templates/view.html',context)
def view(request):
     problem=problems.objects.all()
     context={
        'problems':problem
    }
    #print(context)
    #return render(request,'viewbooks.html',context)
     return render(request,'view.html',context)
def welcome(request):
     return render(request,'welcome.html')
def nur(request):
     return render(request,'nur.html')
def addprob(request):
     submitted=False
     if request.method=='POST':
          form=problemform(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('addprob?submitted=True')
     else:
          form=problemform
          if 'submitted' in request.GET:
               submitted=True

          
     return render(request,'addprob.html',{'form':form ,'submitted':submitted})
def Feedback(request,id=0):
     problem=problems.objects.get(prob_id=id)
     #form=bookform(request.POST or None,instance=modify)
     #if form.is_valid():
        #form.save()
        #return redirect('viewbooks')
     context={
          'problem':problem
     }
     return render(request,'feedback.html',context)

#      all=problems.objects.all()
#      context={
#         'problems':problems,
#         #'form':form
        
#     }
#      return render(request,'updatebook.html',context)
def fsubmit(request, id):
     # Get the problem with the id passed to the view
     myid= problems.objects.get(pk=id)
     context = {'problem': myid}
     if request.method=='POST':
          feedbackk=request.POST['feedback']          
          newfeedback=feedback(myfeedback=feedbackk ,prob_id=myid)
          newfeedback.save()
          return HttpResponse('Submitted Succesfully .Thankyou for your feedback!!')
     return render(request,'feedback.html', context= context)
def schedule(request,id=0):
     problem=problems.objects.get(prob_id=id)
     context={
          'problem':problem
     }
     return render(request,'schedule.html',context)
def delete (request ,id=0):
     if id:
        try:
            remove=problems.objects.get(prob_id=id)
            remove.delete()
            #return HttpResponse('Deleted Succesfully.please refresh the page ')
            return redirect('/view')

        except:
            return HttpResponse('enable to delete please try again later ')

#      problem=problems.objects.all()
#      context={
#         'problems':problem
#     }
#      return render(request,'view.html',context)
def modify(request,id):
     modify=problems.objects.get(pk=id)
     form=problemform(request.POST or None,instance=modify )
     if form.is_valid():
          form.save()
          return redirect('/view')

     problem=problems.objects.all()
     context={
        'problems':problem,
        'form':form
    }
     return render(request,'update.html',context)

def adminlogin(request):
     if request.method=='POST':
          
          username=request.POST['username']
          password=request.POST['password']
          user=myuser.objects.filter(username=username,password=password)
          if request.user.is_superuser:
               return redirect('welcome')
     return render(request,'adminlogin.html')
def startworking(request,id):

     print(id)
     new=problems.objects.get(pk=id)
     if request.method=='POST':
          estdate=request.POST['ed']
          print(estdate)
          startdate=request.POST['sd']
          print(startdate)
          new.ecompletiondate=estdate
          new.startdate=startdate
          print("hello")

          new.save()
          print("saved")
     else:
          print("in else loop rn ")
          
     context={'problem':new}
     return render (request,'startworking.html',context)




     
          
     


