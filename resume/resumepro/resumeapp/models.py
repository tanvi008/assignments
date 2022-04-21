from django.db import models

# Create your models here.
#anything you create here will be stored in database so create fields you want to store in your dtabase


class UserInfo(models.Model):
    name=models.CharField(max_length= 200, blank=True, null=True) 
    email= models.EmailField(max_length=200, blank=True, null=True)
    technicalskill = models.CharField(max_length=500, blank=True, null=True)
    workexperience = models.CharField(max_length=200, blank=True, null=True)
    courses = models.CharField(max_length=200, blank=True, null=True)
    projects=models.CharField(max_length=200, blank=True, null=True)
    awards= models.CharField(max_length=200, blank=True, null=True)
    summary=models.TextField(blank=True, null=True)
    educationdetail =models.TextField(blank=True, null=True) 
    careerobjective =models.TextField(blank=True, null=True)
    other=models.CharField(max_length=200,blank=True, null=True)
    


class pdf(models.Model):
    document = models.FileField(upload_to = 'pdf/')
    # users = models.ManyToManyField(UserInfo)
