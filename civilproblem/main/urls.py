from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'civilproblem_main'
urlpatterns = [
    path('adminlogin',views.adminlogin,name='adminlogin'),
     
    path('notsolved',views.notsolved,name='views.notsolved'),
    path('progress',views.progress,name='views.progress'),
    path('complete',views.complete,name='views.complete'),
    path('view',views.view,name='views.view'),
    path('welcome',views.welcome,name='views.welcome'),
    path('nur',views.nur,name='nur'),
    path('addprob',views.addprob,name='views.addprob'),
    path('feedback/<int:id>',views.Feedback,name="views.Feedback"),
    path('feedback/fsubmit/<int:id>/',views.fsubmit,name='fsubmit'),
    path('schedule/<int:id>',views.schedule,name='views.schedule'),
    path('delete/<int:id>',views.delete,name='views.delete'),
    path('modify/<int:id>',views.modify,name='views.modify'),
    path('adminlogout',views.adminlogout,name='views.adminlogout'),
    path('searchproblem',views.searchproblem,name='views.searchproblem'),
    path('startworking/<int:id>',views.startworking,name='startworking')

    

    
    
]