from django.urls import path
from django.urls import path, include # new
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'polls'

urlpatterns = [
    #path('', views.index, name='index'),
    path('login/', views.login, name='login'),
   
	path('doLogin', views.doLogin, name='doLogin'),
	path('register', views.register, name='register'),
	path('doRegister', views.doRegister, name='doRegister'),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('home', views.home, name = 'home'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('index', views.index, name = 'index'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
