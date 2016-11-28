from django.shortcuts import render
import os
from django.http import HttpResponse

from .models import Greeting

def index(request):
    return render(request, 'index.html')

def names(request):
    return render(request, 'names.html')

def flagged(request):
    return render(request, 'flagged.html')

def contact(request):
    return render(request, 'contact.html')


