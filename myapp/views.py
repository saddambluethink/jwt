from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import employee
from .serializers import employeeSerializer
#from rest_framework.parsers import JSONParser
#import io

# API authentication 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class class_Base_API(APIView):
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            try:
                stu=employee.objects.get(id=id)
                serilizer=employeeSerializer(stu)
                return Response(serilizer.data)
            except:
                res={'msg':'data not found'}
                return Response(res,status.HTTP_404_NOT_FOUND)    
        emp1=employee.objects.all()
        serilizer=employeeSerializer(emp1,many=True)
        return Response(serilizer.data)  
        

        
        #add data
    def post(self,request,format=None):
        sr=employeeSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)

     #updete data by put
    def put(self,request,pk=None,format=None):
        id=pk
        stu=employee.objects.get(id=id)
        sr=employeeSerializer(stu,data=request.data)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)

     # patch update data 
    def patch(self,request,pk=None,format=None):
        id=pk
        stu=employee.objects.get(id=id)
        sr=employeeSerializer(stu,data=request.data,partial=True)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created partial'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)



     # delete data
    def delete(self,request,pk=None,format=None):
        id=pk
        try:
            stu=employee.objects.get(id=id)
            stu.delete()
            return Response({'msg':'data deleted'}, status=status.HTTP_201_CREATED)
        except:
            res={'msg':'data not deleted becouse this id not in database'}
            return Response(res,status.HTTP_404_NOT_FOUND)








