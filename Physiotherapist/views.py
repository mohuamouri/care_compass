from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Physiotherapist
from .serializers import PhysiotherapistSerializer

@api_view(['POST', 'GET'])
def physiotherapist_data(request):
    try:
        if request.method == 'POST':
            serializer = PhysiotherapistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Physiotherapist data saved successfully.",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            # Only fetch approved physiotherapists
            physiotherapists = Physiotherapist.objects.filter(is_approved=True)

            if not physiotherapists.exists():  # Check if no approved physiotherapists exist
                return JsonResponse({
                    "message": "No approved physiotherapists available."
                }, status=status.HTTP_200_OK)

            serializer = PhysiotherapistSerializer(physiotherapists, many=True)
            return JsonResponse({
                "message": "Approved physiotherapist data retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK, safe=False)

    except Exception as e:
        return JsonResponse({
            "error": "An error occurred.",
            "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
