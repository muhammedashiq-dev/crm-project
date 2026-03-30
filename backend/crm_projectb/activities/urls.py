from django.urls import path
from . import views 

urlpatterns = [
    path('activities',views.activity_list,name='activity-list'),
    path('activities/<int:pk>/',views.activity_detail,name='actvity-detail'),
    path('activites/<int:pk>/mark-completed/',views.mark_completed,name='mark-completed'),
    path('activities/upcoming/',views.upcoming_activities,name='upcoming-activities'),
]
