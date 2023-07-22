from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.

class CreateJobListing(APIView):
    def post(self, request, *args, **kwargs):
         return HttpResponse(status=201)

class JobList(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=200)