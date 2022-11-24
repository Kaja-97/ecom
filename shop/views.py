from django.shortcuts import render,redirect
from . models import *
from django . contrib import messages
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    products=Product.objects.filter(status=0,trending=1).all()
    seller=Seller.objects.filter().first()
    return render(request,"shop/index.html",{"products":products,"seller":seller})



def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:

        if request.method=='POST':
            username=request.POST.get('username')
            pwd=request.POST.get('password')

            user=authenticate(request,username=username,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User name password")
                return redirect("/login")
        
    return render(request,"shop/login.html")
    
   

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You are Logged out")
        return redirect("/login")
    else:
        messages.success(request,"You already Logged out")
        return redirect("/")
        


def about(request):
    return render(request,"shop/About.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success You can login now")
            return redirect('/register')
    return render(request,"shop/register.html",{'form':form})

def Sell(request):
    return render(request,"shop/addproduct.html")

def Products(request):

    catagory=Catagory.objects.filter(status=0)

    return render(request,"shop/Products.html",{"catagory":catagory})


def Productpage(request,name):
    
    if(Catagory.objects.filter(name=name,status=0)):
        product=Product.objects.filter(Catagory__name=name).all()
        return render(request,"shop/products/index.html",{"product":product,"catyagory_name":name})
    else:
        messages.warning(request,"No Such Catagory found")
        return redirect ('Products')



        
def Product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            
            product=Product.objects.filter(name=pname,status=0).first()
            
            seller=Seller.objects.filter(name=product.Seller_ID).first()

            return render (request,'shop/products/Product_details.html',{"product":product,"seller":seller})
        else:
            messages.warning(request,"No Such Catagory found")
            return redirect ('Products')
    
    else:
        messages.warning(request,"No Such Catagory found")
        return redirect ('Products')


        
def Allproduct(request):
    catagory=Product.objects.filter(status=0)
    return render(request,"shop/index.html",{"catagory":catagory})