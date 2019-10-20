from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Layout


def index(request):
    return HttpResponse("Test get layout requests")


def layout(request, layoutName):
    resquested_layout = get_object_or_404(Layout, name=layoutName)

    return HttpResponse("Here your layout : "+resquested_layout)

# Create your views here.
