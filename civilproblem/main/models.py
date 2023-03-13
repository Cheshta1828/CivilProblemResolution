from django.db import models
from datetime import datetime,date

# Create your models here.
class problems(models.Model):
    COMPLETED = 'CC'
    PENDING = 'IC'
    PROGRESS= 'IP'
    CHOICES = [
        (COMPLETED, 'CC'),
        (PENDING, 'IC'),
        (PROGRESS, 'IP'),]
    prob_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=5000)
    
    postedby=models.CharField(max_length=50)
    location=models.CharField(max_length=50, default="")
    votes=models.IntegerField()
    status=models.CharField(
        max_length=2,
        choices=CHOICES,
        default=COMPLETED,
    )
    postdate=models.DateField("postdate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)
    startdate=models.DateField("startdate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    ecompletiondate=models.DateField("ecompletiondate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    acompletiondate=models.DateField("acompletiondate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    def __str__(self):
        return self.title
class feedback(models.Model):
    myfeedback=models.CharField(max_length=50000)
    
    prob_id=models.ForeignKey(problems,on_delete=models.CASCADE)










    
    
    




    



