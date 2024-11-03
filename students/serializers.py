from rest_framework import serializers
from .models import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        # fields = ["StudentID", "Name", "Dept", "DOB", "Image"]
        fields = "__all__"
