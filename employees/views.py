from django.shortcuts import render

from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['employees']
)
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer