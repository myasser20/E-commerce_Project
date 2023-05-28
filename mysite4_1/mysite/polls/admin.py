from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . models import  Order, OrderItem, Product, UserManager , User

# Register your models here.
#admin.site.register(Signup)

#class AccountInline (admin. StackedInline):
 #odel = Account
 #can_delete = False
 #verbose_name_plural = 'Accounts'

#class Customizeuseradmin (UserAdmin):
 #  inlines =(AccountInline,)



admin.site.register(User)
#admin.site.register(User,Customizeuseradmin)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
#admin.site.register(Account)
 

