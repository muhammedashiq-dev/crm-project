from django.db import models
from accounts.models import User
from customers.models import Customer

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new','New'),
        ('qualified','Qualified'),
        ('converted','Converted'),
        ('lost','Lost')
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="new")
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="leads")
    to_customer = models.OneToOneField(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    