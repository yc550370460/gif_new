from django.shortcuts import render
from django.http import HttpResponse
from gif_app.models import Image
from django.conf import settings
import os
import json
import random

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
    all_object = Image.objects.all()
    image_object = all_object.order_by("weight")[page_number:page_number+1]
    if image_object.exists():
        path = image_object[0].path
    else:
        id_list = all_object.values("id")
        tmp_number = random.randint(0, len(id_list) - 1)
        path = all_object.order_by("weight")[tmp_number:tmp_number+1][0].path

    return render(request, "index.html", {'image_path': path})

def upload(request):
    pass