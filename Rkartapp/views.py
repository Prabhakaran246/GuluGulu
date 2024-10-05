from django.shortcuts import redirect,render
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout Successfully..!")
        return redirect("home")
    else:
        messages.error(request,"No Login found..!")
        return redirect("home")

def login_page(request):
    form=CustomUserForm()
    if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password1')
        user=authenticate(username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully..!")
            return redirect('home')
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect('login')
    return render(request,"shop/login.html",{'form':form})
    
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull ! You can Login now..")
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"category":category})

def collectionsview(request,name):
    if (Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name,status=0)
        return render(request,"shop/collections/index.html",{"products":products,"name":name})
        

def product_details(request,cname,pname):
    if (Category.objects.filter(name=cname,status=0)):
        if (Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/collections/products.html",{"products":products,"name":pname})