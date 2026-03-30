from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['POST','GET'])
def activity_list(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        
        activity_type = request.query_params.get('type')
        lead_id = request.query_params.get('lead')
        completed = request.query_params.get('completed')
        
        if activity_type:
            activities = activities.filter(activity_type = activity_type)
        if lead_id:
            activities = activities.filter(lead_id = lead_id)
        if completed:
            activities = activities.filter(completed = completed.lower() == 'true')
            
        serializer = ActivitySerializer(activities, many=True)  
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ActivitySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT','GET','DELETE'])
def activity_detail(request,pk):
    activity = get_object_or_404(Activity,pk=pk)  
    
    if request.method == 'GET':
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ActivitySerializer(instance = activity, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PATCH'])
def mark_completed(request,pk):
    activity = get_object_or_404(Activity,pk=pk) 

    activity.completed = True
    activity.save()
    return Response({'status' : 'Activity marked as complete'})

@api_view(['GET'])
def upcoming_activities(request):
    from django.utils import timezone
    activities = Activity.objects.filter(
        scheduled_at__gte = timezone.now(),
        completed = False
    ).order_by('scheduled_at')
    
    serializer = ActivitySerializer(activities,many=True)
    return Response(serializer.data)