from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("123")
    return render(request, "test.html")

def gif(request):
    # return HttpResponse("123")
    return render(request, "index.html")