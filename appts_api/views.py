from django.shortcuts import render
from rest_framework import generics
from .serializers import ApptSerializer
from .models import Appt
# Create your views here.

class ApptList(generics.ListCreateAPIView):
    queryset = Appt.objects.all().order_by('id')
    serializer_class = ApptSerializer
# this is for post and get

class ApptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appt.object.all().order_by('id')
    serializer_class = ApptSerializer
# get, delete, put
