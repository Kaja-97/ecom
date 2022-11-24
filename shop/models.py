from django.db import models
import datetime
import os
import random
from django.contrib.auth.models import User

def getFilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d:%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('upload/',new_filename)

class Catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFilename)
    description = models.TextField(max_length=60,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    created_at = models.DateField(auto_now_add=True)


    def __str__(self) :
        return self.name


class Seller(models.Model):
    def random():
        return random.randint()

    Seller_ID = models.IntegerField(null=False,blank=False,primary_key=True)
    name = models.CharField(max_length=150,null=False,blank=False)
    Seller_image = models.ImageField(upload_to=getFilename)
    age =  models.IntegerField(null=False,blank=False)
    place =  models.CharField(max_length=50, null=False,blank=False)
    address =  models.TextField(null=False,blank=False)
    NIC_Number = models.CharField(max_length=12,null=False,blank=False)
    Phone_Number = models.CharField(max_length=15,null=False,blank=False)
    Email = models.CharField(max_length=150,null=False,blank=False,unique=True)
    DOB = models.DateField()
    


    def __str__(self) :
        return self.name



class Product(models.Model):
    Catagory  = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    Seller_ID = models.ForeignKey(Seller,on_delete=models.CASCADE)
    # Product_ID = models.IntegerField(null=True,blank=True)
    name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getFilename)
    old_price =  models.FloatField(null=False,blank=False)
    new_price =  models.FloatField(null=False,blank=False)
    selling_price =  models.FloatField(null=False,blank=False)
    stock = models.IntegerField(default=1)
    description = models.TextField(max_length=1500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-defoult,1-trending")
    created_at = models.DateField(auto_now_add=True)


    def __str__(self) :
        return self.name

# Create your models here.

# class user(models.Model):
#     def random():
#         return random.randint()

#     User_ID = models.IntegerField(null=False,blank=False,primary_key=True)
#     username = models.CharField(max_length=150,null=False,blank=False)
#     User_img = models.ImageField(upload_to=getFilename)
#     age =  models.IntegerField(null=False,blank=False)
#     place =  models.CharField(max_length=50, null=False,blank=False)
#     address =  models.TextField(null=False,blank=False)
#     NIC_Number = models.CharField(max_length=12,null=False,blank=False)
#     Phone_Number = models.CharField(max_length=15,null=False,blank=False,unique=True)
#     Email = models.CharField(max_length=150,null=False,blank=False,unique=True)
#     DOB = models.DateField()
#     Password=models.CharField(max_length=150,null=False,blank=False)


#     def __str__(self) :
#         return self.name
