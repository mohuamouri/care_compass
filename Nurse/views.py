from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Nurse
from .serializers import NurseSerializer

@api_view(['POST', 'GET'])
def nurse_data(request):
    try:
        if request.method == 'POST':
            serializer = NurseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Nurse data saved successfully.",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            # Only fetch approved nurses
            nurses = Nurse.objects.filter(is_approved=True)

            if not nurses.exists():  # Check if no approved nurses exist
                return JsonResponse({
                    "message": "No approved nurses available."
                }, status=status.HTTP_200_OK)

            serializer = NurseSerializer(nurses, many=True)
            return JsonResponse({
                "message": "Approved nurse data retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK, safe=False)

    except Exception as e:
        return JsonResponse({
            "error": "An error occurred.",
            "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
