from imp import NullImporter

from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from django.template import context
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string

#translating
from django.utils.translation import gettext as _
#from django.utils.translation import get_language, activate, gettext
from django.views.decorators.csrf import requires_csrf_token

#     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 





# Create your views here.


def store(request):
    
    return render(request, 'store/index.html')


def izdavastvo(request):
    izdavastvo = Izdavastvo.objects.all()
    if request.user.is_authenticated:
            customer = Customer.objects.get(name=request.user.username)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
    else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']

    context = {'izdavastvo': izdavastvo,'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/izdavastvo.html', context)


def priceSaTerena(request):
    return render(request, 'store/priceSaTerena.html')

def psenicaikvalitetbrasnaprica(request):
    return render(request, 'store/pricesaterenatekstovi/psenicaikvalitetbrasnaprica.html')



def mlin(request):
    return render(request, 'store/mlin.html')

def trgovina(request):   
        products = Product.objects.all()
        if request.user.is_authenticated:
            customer = Customer.objects.get(name=request.user.username)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']

        context = {'products': products,'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'store/trgovina.html', context)


def searchProducts(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:

            products = Product.objects.filter(name__contains = searched)
            context = {'products': products}
            return render(request, 'store/searchProducts.html', context)
        else:
            products = Product.objects.all()
            customer = Customer.objects.get(name=request.user.username)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items

        context = {'products': products,'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'store/trgovina.html', context)
        
  

def pecanje(request):
    return render(request, 'store/pecanje.html')

def pesme(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'store/pesme.html', context)

def kontakt(request):
    return render(request, 'store/kontakt.html')

def kurs(request):
    return render(request, 'store/kurs.html')

def kursTehnologije(request):
    return render(request, 'store/kursTehnologije.html')

def cart(request):
    
    if request.user.is_authenticated:
        #print(request)
        #customer = Customer.objects.first() # hacked
        customer = Customer.objects.get(name=request.user.username)
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request,('store/cart.html'), context)

@requires_csrf_token
def checkout(request):
    if request.user.is_authenticated:
        
        customer = Customer.objects.get(name=request.user.username)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        cartList = order.get_cart_list
        

        html_message = render_to_string('store/podaciokorisniku.html', {'user': request.user, 'email': request.user.email, 'grad': request.user.first_name, 'adresa': request.user.last_name, 'total': order.get_cart_total, 'ukupnoukorpi': order.get_cart_items, 'stvariukorpi': cartList})
       
        #da bi ti ovaj render to string radio i da bi dobio u mejlu ime logovanog korisnika itd, drugi argument tj ovo u navodnicima mora biti isto kao ono sto renderujes u zagradama u podaciokorisniku.html! npr moras imati {'user': request.user}, pa onda u onom html fajlu da imas {{user}}
        
        

        #sto se tice state city i adress, kada ukucavas ove podatke kada se registrujes, sajt ih nece uopste uvaziti i davace stalno istu adresu customera (srbija, novi sad, rumenacka 108)!       
        
#sending an email
        email = EmailMessage(
            'Podaci o korisniku',
            html_message,
            settings.EMAIL_HOST_USER,
            ['darko.spasojevic.django24@gmail.com'],
        )
        
        email.fail_silently = False
        email.send()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request,('store/checkout.html'), context)

def updateItem(request):
    data = json.loads(request.body)
    
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('productId:', productId)

    customer = Customer.objects.get(name=request.user.username)
    product = Product.objects.get(id=productId)
    instock = product.instock
        
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        if orderItem.quantity >= instock:
             messages.info(request, 'Out of stock')
             #return render(request, 'store/cart.html')
        else:
            orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    
    return JsonResponse('item was added', safe=False)


@requires_csrf_token
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            customer = Customer(name=user)
            customer.save()
            messages.success(request, 'Account was created for user ' + user)
            return redirect('loginPage')

    context = {'form': form}
    return render(request, ('store/registerPage.html'),context)


@requires_csrf_token
def loginPage(request):
    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('trgovina')
            else:
                messages.info(request, 'Username or password is incorrect')


        context = {}
        return render(request, ('store/loginPage.html'), context)

def logoutPage(request):
    logout(request)
    #Problem: ocu da kada se logoutujem da obrisem svoj order i stvari u korpi.
    # Problem je taj sto kada se jedan user logoutuje, drugom useru ostaju iste stvari u korpi 
    return redirect('/')
