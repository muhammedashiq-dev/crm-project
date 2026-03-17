from django.db import models
from accounts.models import User
from leads.models import Lead

class Activity(models.Model):
    ACTIVITY_TYPE = [
        ('calls', 'Calls'),
        ('meeting','Meeting'),
        ('emails','Emails'),
        ('follow_up','Follow Up')
    ]
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=20,choices=ACTIVITY_TYPE)
    lead = models.ForeignKey(Lead,on_delete=models.CASCADE,null=True,blank=True,related_name='activities')
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title