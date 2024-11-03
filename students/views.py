from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets, pagination

# Create your views here.

class PageSizePagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "size"


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('-id')
    serializer_class = StudentsSerializer
    # pagination_class = PageSizePagination
