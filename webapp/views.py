from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializer import employeeSerializer

class emplist(APIView):
    def get(self, request):
        allemp= employee.objects.all()
        srl= employeeSerializer(allemp, many= True)
        return Response(srl.data)

