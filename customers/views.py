from django.shortcuts import render

from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['customers']
)
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
