from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        pass
        # id_list = all_object.values("id")
        # tmp_number = random.randint(0, len(id_list) - 1)
        # path = all_object.order_by("weight")[tmp_number:tmp_number+1][0].path

    return render(request, "index.html", {'image_path': path})


def manage(request):
    return render(request, "manage.html")


def upload(request):
    try:
        file = request.FILES
        basic_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        store_file_name = os.path.join(basic_dir, "static", "img", request.FILES["file"].name)
        if os.path.exists(store_file_name):
            return HttpResponse(json.dumps({"status": -1, "description": "file already exist"}))
        with open(store_file_name,"wb+") as f:
            for chunk in file["file"].chunks():
                f.write(chunk)
        new_obj = Image.objects.create(status="OK", active=True, path="../static/img/" + request.FILES["file"].name,
                                       name=request.FILES["file"].name, weight=0)
        new_obj.save()
        return HttpResponse(json.dumps({"status": 0, "description": "Upload successfully"}))
    except Exception, e:
        return HttpResponse(json.dumps({"status": -1, "description": "inner error"}))