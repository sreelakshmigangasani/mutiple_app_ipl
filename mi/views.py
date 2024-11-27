from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hardik(request):
    return HttpResponse('<h1>hardik will return as captain of mi in ipl</h1>')

