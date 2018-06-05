from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from food.nalclient import NALClient


_client = NALClient(os.environ['NAL_API_KEY'])

# Create your views here.

def index(request):
    return HttpResponse("What up")


def search(request):
    if 'q' not in request.GET:
        return HttpResponse('q parameter is required', status=400)
    return JsonResponse(_client.search(request.GET.get('q')))

