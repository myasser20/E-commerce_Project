from multiprocessing import AuthenticationError
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render , get_object_or_404
from . models import Product,User ,Order,OrderItem 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
#from django.contrib.auth.models import  User
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def shop(request):
 p2 = Product.objects.all()
 context = {'products':p2}
 return render(request,'shop.html',context)

def index2(request):
    return render(request, 'index.html')

def sproduct(request,id):
    print ('test functionality for sproduct')
    products = get_object_or_404(Product,pk=id)
    context = {'prname':products.name,
               'prprice':products.price,
               'primg':products.image,
               'prId':id
    } 
    return render(request, 'sproduct.html', context)

def cart(request): 
    order = Order.objects.get(customer=request.user)
    products = OrderItem.objects.filter(order=order).all()
    context = {'products':products, }
    return render(request, 'cart.html', context)

def add_to_cart(request,id):
    print ('test functionality for add_to_cart')
    pro = get_object_or_404(Product, pk=id)
    currentOrder,createdOrder= Order.objects.get_or_create(customer=request.user, complete=True)
    if  createdOrder == False :
        getCurrentOrderItem, createdOrderItemStatus= OrderItem.objects.get_or_create(product=pro, order=currentOrder)
        currentOrderItem = getCurrentOrderItem
        currentOrderItem.quantity+=1
        currentOrderItem.save()
        return redirect('cart')
    else :  
        orderItem = OrderItem(product=pro,
                            order=currentOrder,
                            quantity=1) 
        orderItem.save()
        messages.success(request, "Cart updated!")
        return redirect('cart')

def cart_remove(request,id):
    cartitem=get_object_or_404(OrderItem,pk=id)
    if cartitem.quantity >1:
       cartitem.quantity-=1
       cartitem.save()
       return redirect('cart')
    else:   
        cartitem.delete()
        return redirect('cart')

def contact(request):
    return render(request, 'contact.html')
                                
def home(request): 
   if request.method =='POST':
      youraddress=request.POST.get('address')
      youremail=request.POST.get('email')
      yourpassword=request.POST.get('password')
      check =User.objects.filter(username=youremail).exists()
      if check:
           messages.error(request, 'Email is already exists')
           return redirect('/signup')
      else:
        data=User.objects.create_user(address=youraddress,email=youremail,password=yourpassword)
        data.set_password(yourpassword)
        data.save()
        return render(request,'index.html') 
   else:
     return render(request,'index.html')

   
def login_user(request):
 if request.method =='POST':
     yourusername = request.POST["username"]
     yourpassword = request.POST["password"]
     user = authenticate(request, username=yourusername, password=yourpassword)
     if user is not None:
         login(request, user)
         # Redirect to a success page.
         return render(request,'index.html')
     else:
        # Return an 'invalid login' error message.
        messages.error(request,('Invalid Email or Password'))
        return redirect('/signup')
 else:
     return render(request,'/signup')

def logout_user(request):
   logout(request)
   messages.success(request,('You are now logged out'))
   return redirect("/")
        



