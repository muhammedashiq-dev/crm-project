from django.db import models
from accounts.models import User
from leads.models import Lead

class Activity(models.Model):
    ACTIVITY_TYPE = [
        ('call', 'Call'),
        ('meeting','Meeting'),
        ('emails','Emails'),
        ('follow_up','Follow Up')
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    activity_type = models.CharField(max_length=20,choices=ACTIVITY_TYPE)
    lead = models.ForeignKey(Lead,on_delete=models.CASCADE,null=True,blank=True,related_name='activities')
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='activities')
    scheduled_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['scheduled_at']
        verbose_name_plural = 'Activities'
        
    def __str__(self):
        return self.title