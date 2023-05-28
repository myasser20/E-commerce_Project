from audioop import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings
from django.forms import ValidationError
# Create your models here.
 
class UserManager(BaseUserManager):
  def _create_user(self,email,password,**extrafields):
    email=self.normalize_email(email)
    user=self.model(username=email,**extrafields)
    if not password:
      raise ValidationError("Password required")
    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_user(self,email,password=None,**extrafields):
    return self._create_user(email,password,**extrafields)
  
  def create_superuser(self,email,password,**extrafields):
    user=self._create_user(email=email,password=password,is_staff=True,is_superuser=True)
    return user


class User( AbstractUser,PermissionsMixin):
  address = models.CharField(max_length=60,blank=True)
  is_active=models.BooleanField(default=True)
  is_staff=models.BooleanField(default=False) 
  objects=UserManager()
  
  
  REQUIRED_FIELDS=['email']

  

  def __str__(self):
    return self .username


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
   
def get_absolute_url(self):
      return reverse("product-detail", args=[self.id])

def __str__(self):
		   return self.name
        
  
  
class Order(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
	
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)



	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total




