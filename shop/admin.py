from django.contrib import admin
from . models import *

class Categoryadmin(admin.ModelAdmin):
    list_display = ('name','image')

class productadmin(admin.ModelAdmin):
    list_display = ('name','Seller_ID')

class Selleradmin(admin.ModelAdmin):
    list_display = ('name','Seller_ID')



admin.site.register(Catagory,Categoryadmin)
admin.site.register(Product,productadmin)
admin.site.register(Seller,Selleradmin)



# Register your models here.user
