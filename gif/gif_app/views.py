from django.shortcuts import render
from django.http import HttpResponse
from gif_app.models import Image
from django.conf import settings
import os
import json

# Create your views here.


def index(request):
    # return HttpResponse("123")
    return render(request, "test.html")


def gif(request):
    page = request.build_absolute_uri().split("/")[-1]
    if page.isdigit():
        page_number = int(page)
    else:
        page_number = 1
    print page_number
    all_object = Image.objects.all()
    print [item for item in all_object.order_by("weight")]
    image_object = all_object.order_by("weight")[page_number:page_number+1]
    if image_object.exists():
        path = image_object[0].path
    else:
        path = Image.objects.filter(id=page_number)[0].path

    return render(request, "index.html", {'image_path': path})

def upload(request):
    pass