from rest_framework import serializers
from .models import Nurse

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'  # Include all fields in the model
