from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import ProductUser
import requests
import asyncio
import aiohttp
# Create your views here.

async def main(product_id):

    async with aiohttp.ClientSession() as session:

        url = 'http://127.0.0.1:8000/api/products/{product_id}/likes'
        async with session.get(url) as resp:
            like = await resp.json()
            print(like['message'])



def like (request, product_id):
    req = requests.get('http://127.0.0.1:8000/api/user')
    json = req.json()
    print(json)
    try:
        ProductUser.objects.create(user_id=json['id'],product_id=product_id)
        asyncio.run(main(product_id))
    except Exception as e:
        print(e)
        data = {'message':'Already liked','status_code':208}
        return JsonResponse( data)
    data = {'message':'success','status_code':200}
    return JsonResponse(data)    
    
