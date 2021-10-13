from rest_framework import serializers
#from rest_framework import employee
from .models import employee

# Serializers define the API representation.
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        #fields = ['name', 'lastname', 'email','emid']

        fields= '__all__'