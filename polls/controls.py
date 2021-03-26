from django.shortcuts import render
from .forms import NameForm, LoginForm, RegistrationForm
from django.http import HttpResponse
from .models import Customer, Fullname, Address
from .forms import NameForm
from django.http import HttpResponseRedirect

def login(user, password):
    cus = Customer.objects.raw("SELECT * FROM customer WHERE username = %s AND password=%s",[user,password])
    #print(cus[0].username)
    if len(cus)>0:
        return HttpResponse("success")
    return HttpResponseRedirect("/polls/login")

def register(customer, fullname):
    
    cus = Customer.objects.raw("SELECT * FROM customer WHERE username = %s AND password=%s",[customer.username,password.username])
    #print(cus[0].username)
    if len(cus)>0:
        return HttpResponseRedirect("/polls/register")
    customer.save()
    return HttpResponseRedirect("/polls/login")