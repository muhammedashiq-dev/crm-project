from django.urls import path 
from . import views

urlpatterns = [
    path('customers/',views.customer_list),
    path('customers/<int : pk>'),
]
