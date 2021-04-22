from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def api(request):
    data = {'id': 1, 'name': 'hoge'}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str)
    return response
