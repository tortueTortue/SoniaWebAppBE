from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Test get layout requests")

# Create your views here.
