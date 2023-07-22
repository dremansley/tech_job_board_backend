from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_job_listing(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    return HttpResponse(status=201)
    
@login_required
def list_jobs(request):
    if request.method != 'GET':
        return HttpResponse(status=400)
    return HttpResponse(status=200)
