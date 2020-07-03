from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from core.models import Customer
from rest_framework import viewsets
from core.serializers import CustomerSerializer

class CustomerList(ListView):
    model = Customer
    paginate_by = 10

class CutomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.get_customers()
    serializer_class = CustomerSerializer