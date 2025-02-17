from rest_framework import serializers
from .models import Physiotherapist

class PhysiotherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physiotherapist
        fields = '__all__'  # Include all fields in the model
