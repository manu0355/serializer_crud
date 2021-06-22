from django.shortcuts import render
from serialcrud.models import EmployeeModel,Company
from serialcrud.serializer import EmployeeSerializer,CompanySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Employeedetails(APIView):
    def get(self,request):
        empobj= EmployeeModel.objects.all()
        empserializeobj= EmployeeSerializer(empobj,many=True)
        return Response(empserializeobj.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializeobj= EmployeeSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data, status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeView(APIView):
        
    def get(self,request,pk):
        try:
            empobj = EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            return Response("please pass valid employee id", status= status.HTTP_400_BAD_REQUEST)
        serializeobj=EmployeeSerializer(empobj)
        return Response(serializeobj.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        empobj=EmployeeModel.objects.get(pk=pk)
        empserialobj=EmployeeSerializer(empobj, data=request.data)
        if empserialobj.is_valid():
            empserialobj.save()
            return Response(empserialobj.data, status=status.HTTP_201_CREATED)
        return Response("please update valid details", status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        empobj= EmployeeModel.objects.get(pk=pk)
        empobj.delete()
        return Response("deleted successfulluy", status=status.HTTP_204_NO_CONTENT)