from django.shortcuts import render
from .forms import NameForm, LoginForm, RegistrationForm, BookCreate
from . import controls
from django.http import HttpResponse
from .models import Customer, Fullname, Address, Item, Order, Cart
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
    request.session['username'] = user
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
   
    shelf = Item.objects.all()
    return render(request, 'views/home.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/upload_form.html', {'upload_form':upload})

def addToCart(request, itemid):
    username = request.session['username']
    customer = Customer.objects.filter(username=username)
    item = Item.objects.filter(id=itemid)
    order = Order.objects.create(customerid=customer[0])
    order.save()
    cart = Cart.objects.create(orderid=order,itemid=item[0])
    cart.save()
    return HttpResponse(customer[0].id)

