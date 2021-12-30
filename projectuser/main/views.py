from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import ProductUser
from .producer import publish
import requests
import asyncio
import aiohttp


def like(request, product_id):
    req = requests.get("http://127.0.0.1:8000/api/user")
    json = req.json()
    try:
        ProductUser.objects.create(user_id=json["id"], product_id=product_id)
        publish('product_liked', product_id)
    except Exception as e:
        print(e)
        data = {"message": "Already liked", "status_code": 208}
        return JsonResponse(data)
    data = {"message": "success", "status_code": 200}
    return JsonResponse(data)
