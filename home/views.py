from functools import partial
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import University
from home.serializers import UniversitySerializer


#for display of universities
from rest_framework import viewsets
from django.shortcuts import render
import requests


# Create your views here.


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def university(request):
    if request.method == 'GET':
        if not request.data:
            objs = University.objects.all()
            serializer=UniversitySerializer(objs, many = True)
            return Response(serializer.data) 
        else:
            data=request.data
            obj=University.objects.get(id=data['id'])
            serializer=UniversitySerializer(obj)
            return Response(serializer.data)
    elif request.method == 'POST':
        data=request.data
        serializer=UniversitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT': #doesn't support partial update
        data=request.data
        serializer=UniversitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':  #suppors partial update
        data=request.data

        obj=University.objects.get(id=data['id'])

        serializer=UniversitySerializer(obj,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method=='DELETE':
        data=request.data
        obj=University.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'University deleted'})

#get data from database      
class PostViewSet(viewsets.ModelViewSet):
    queryset=University.objects.all().order_by('name')
    serializer_class=UniversitySerializer

def listu(request):
    response=requests.get('http://127.0.0.1:8000/api/university/')
    data=response.json()
    return render(request,'listu.html',{'data':data})