from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer


@api_view(['POST', 'GET'])
def doctor_data(request):
    try:
        if request.method == 'POST':
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Doctor data saved successfully.",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            # Only fetch approved doctors
            doctors = Doctor.objects.filter(is_approved=True)

            if not doctors.exists():  # Check if no approved doctors exist
                return JsonResponse({
                    "message": "No approved doctors available."
                }, status=status.HTTP_200_OK)

            serializer = DoctorSerializer(doctors, many=True)
            return JsonResponse({
                "message": "Approved doctor data retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK, safe=False)

    except Exception as e:
        return JsonResponse({
            "error": "An error occurred.",
            "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
