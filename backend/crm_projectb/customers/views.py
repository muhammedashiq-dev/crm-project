from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['POST','GET'])
def customer_list(request):
    if request.method == 'GET':
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust,many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def customer_detail(request,pk):
    try:
       customer = get_object_or_404(Customer, pk=pk)
    except Customer.DoesNotExist:
        return Response({'error':'Customer not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CustomerSerializer(instance = customer,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response({'message' : 'Customer deleted successfully'},status=status.HTTP_200_OK)