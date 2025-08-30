from django.shortcuts import render
from django.http import HttpResponse

# Create your views he e
def learn_python(request):
    return HttpResponse("<h1>Hello world</h1>")

def learn_math(request):
    a = 10
    b = 20
    c = a + b
    return HttpResponse(f"<h1>Answer: {c}</h1>")

def courseOneFn(request):
    return render(request, "course-one.html")