from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def top(request):
    return HttpResponse(b"Hello World")

