from django.db import models
from django.contrib.auth.models import User
from main.models import problems


#Create your models here.
class myuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    adhaar=models.CharField(max_length=19)
    city=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=2000)
    contact=models.CharField(max_length=10)
   


    
def __str__(self) -> str:
        return self.user.username
        



    

    
