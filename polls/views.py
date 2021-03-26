from django.shortcuts import render
from .forms import NameForm, LoginForm, RegistrationForm
# Create your views here.
from django.http import HttpResponse
from .models import Customer, Fullname, Address
from .forms import NameForm
from django.http import HttpResponseRedirect
def index(request):
    return HttpResponse("Hello anh em!!!")

def login(request):
    # if this is a POST request we need to process the form data
    
    form = LoginForm()
    return render(request, 'views/login.html', {'form': form})


def doLogin(request):
    user = request.POST['username']
    password = request.POST['password']
    cus = Customer.objects.raw("SELECT * FROM customer WHERE username = %s AND password=%s",[user,password])
    #print(cus[0].username)
    if len(cus)>0:
        return HttpResponse("success")
    return HttpResponseRedirect("/polls/login")
	
def register(request):
    form = RegistrationForm()
    return render(request, 'views/register.html', {'form': form})

def doRegister(request):
    first
    user = request.POST['username']
    password = request.POST['password']
    cus = Customer.objects.raw("SELECT * FROM customer WHERE username = %s AND password=%s",[user,password])
    #print(cus[0].username)
    if len(cus)>0:
        return HttpResponse("success")
    return HttpResponseRedirect("/polls/login")  
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
        	print ("success")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'name.html', {'form': form})