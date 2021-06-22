from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import sign_up_add
from django.contrib import auth #for login function
# from .forms import
# import sqlite3

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    if request.method=="POST":
        username1= request.POST['username']
        password1= request.POST['password']
        x=auth.authenticate(username=username1, password=password1)
        if x is None:
            return HttpResponseRedirect('signin/')
        else:
            return HttpResponseRedirect('')

def sign_in(request):
    return render(request,'signin.html')



def sign_up(request):
    # first_name=sign_up_add.objects.all()
    # last_name=sign_up_add.objects.all()
    # values={'first_name':first_name, 'last_name':last_name}
    values=sign_up_add.objects.all()
    values={'value':values}
    print (values)
    return render(request,'signup.html' , values)

def add_user(request):
    first_name= request.POST['first_name']
    last_name= request.POST['last_name']
    username= request.POST['username']
    password= request.POST['password']
    confirm_password= request.POST['confirm_password']
    email= request.POST['email']
    mobile_number= request.POST['mobile_number']
    details=sign_up_add(first_name=first_name,last_name=last_name,username=username,password=password,confirm_password=confirm_password,email=email,mobile_number=mobile_number)
    details.save()
    
    # first_name = sign_up_add(first_name= request.POST['first_name'])
    # last_name = sign_up_add(last_name= request.POST['last_name'])
    # username= sign_up_add(username= request.POST['username'])
    # password= sign_up_add(password= request.POST['password'])
    # confirm_password= sign_up_add(confirm_password= request.POST['confirm_password'])
    # email= sign_up_add(email= request.POST['email'])
    # mobile_number= sign_up_add(mobile_number= request.POST['mobile_number'])
    # first_name.save()
    # last_name.save()
    # username.save()  # this will not work
    # password.save()
    # confirm_password.save()
    # email.save()
    # mobile_number.save()
    # adding=''' insert into sign_up_add values(first_name, last_name, username, password); '''
    # sign_up_add.execute(adding)
    return render(request,'registered.html',{'details1': details})

def basic(request):
    return render(request,'base.html')