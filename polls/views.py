from django.shortcuts import render
from .forms import NameForm, LoginForm, RegistrationForm
from . import controls
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
    return controls.login(user,password)
	
def register(request):
    form = RegistrationForm()
    return render(request, 'views/register.html', {'form': form})

def doRegister(request):
    firstname = request.POST['firstname']
    midname = request.POST['midname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    phonenumber = request.POST['phonenumber']
    dob = request.POST['dob']
    user = request.POST['username']
    password = request.POST['password']
    customers = Customer.objects.raw("SELECT ID FROM customer WHERE username = %s ",[user])
    print(len(customers))
    if(len(customers)>0):
        return HttpResponseRedirect("/polls/register")
    cus = Customer.objects.create(phonenumber=phonenumber, email=email, dob=dob, username=user, password=password)
    fullname = Fullname.objects.create(customerid = cus, firstname=firstname, midname=midname, lastname=lastname)

    cus.save()
    #name = Fullname(customerid = customer, firstname = fullname.firstname, midname=fullname.secondname, lastname = fullname.lastname)
    fullname.save()

    return HttpResponseRedirect("/polls/login")
    #print(cus[0].username)
def home(request):
      return render(request, 'views/home.html')
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