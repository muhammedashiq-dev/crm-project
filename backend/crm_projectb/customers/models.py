from django.db import models
from accounts.models import User

class Customer(models.Model):
    STATUS_CHOICES = [
        ('active','Active'),
        ('inactive','Inactive')
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20,blank=True)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="active")
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="customers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"