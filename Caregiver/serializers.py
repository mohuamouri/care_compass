from rest_framework import serializers
from .models import Caregiver

class CaregiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caregiver
        fields = '__all__'  # Include all fields in the model
