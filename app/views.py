from django.shortcuts import render
from django.http import HttpResponse

# Create your views he e
def learn_python(request):
    return HttpResponse("<h1>Hello world</h1>")