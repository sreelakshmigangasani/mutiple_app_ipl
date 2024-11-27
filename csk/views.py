from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ruthuraj(request):
    return HttpResponse('<h1>The team is currently captained by ruthuraj</h1>')
