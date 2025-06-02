from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def new_data(request):
    return HttpResponse("Hello, world. You're at the polls new data.")