from django.urls import path
from . import views

url =[
    path('api/appts', views.ApptList.as_view(), name = 'appt_list'),
    path('api/appts/<int:pk>', views.ApptDetail.as_view(), name = 'appt_detail'),
]
