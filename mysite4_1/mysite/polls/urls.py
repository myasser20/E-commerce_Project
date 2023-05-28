
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('shop',views.shop,name='shop'),
    path('product/<int:id>',views.sproduct,name='product-detail'),
    path('main',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('cart',views.cart,name='cart'),
    path('contact',views.contact,name='contact'),
    path('addToCart/<int:id>',views.add_to_cart,name='addToCart'),
    path('RemoveFromCart/<int:id>',views.cart_remove,name='RemoveFromCart'),
]
