from rest_framework import serializers
from .models import Appt

class ApptSerializer (serializers.ModelSerializer):
    class Meta:
        model = Appt
        fields = '__all__'
