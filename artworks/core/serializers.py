from core.models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','gender','emailid','date_of_birth','contact','address']