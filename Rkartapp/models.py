from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
def getFileName(request,filename):
    newdate=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    newfilename="%s%s"%(newdate,filename)
    return os.path.join('uploads/',newfilename) 

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name