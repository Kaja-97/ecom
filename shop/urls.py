from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns=[
    path('home',views.home,name="home"),
    path('Home',views.home,name="home"),
    path('HOME',views.home,name="home"),
    path('',views.home,name="home"),

    path('About',views.about,name="About"),
    path('login',views.login_page,name="Login"),
    path('logout',views.logout_page,name="Logout"),

    path('register',views.register,name="register"),
    path('Sell',views.Sell,name="Sell"),
    path('Products',views.Products,name="Products"),
    path('Products/<str:name>',views.Productpage,name="Products"),
    path('Products/<str:cname>/<str:pname>',views.Product_details,name="Product_details"),
    
    path('Allproduct',views.Allproduct,name="Allproduct"),
    


    



]

