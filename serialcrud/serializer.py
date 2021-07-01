from .models import EmployeeModel,Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    employee= CompanySerializer(read_only=True, many=True)

    class Meta:
        model = EmployeeModel
        fields = "__all__"