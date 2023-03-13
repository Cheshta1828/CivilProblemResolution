from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('admin/', admin.site.urls),
    # path('',include('user.urls'))

    path('userlogin',views.userlogin,name='userlogin'),
     #path('adminlogin',views.adminlogin,name='adminlogin'),
     path('register',views.register,name='register'),
     path('hello',views.hello,name='hello'),
     path('userview',views.userview,name='userview'),
     path('useraddprob',views.useraddprob,name='useraddprob'),
     path('editprofile/<int:id>',views.editprofile,name='editprofile'),
     path('userlogout',views.userlogout,name='userlogout'),
     path('searchproblem',views.searchproblem,name='views.searchproblem'),
     path('vote/<int:id>',views.vote,name='vote')
    #path('registernew',views.registernew,name='registernew')
        
    
]