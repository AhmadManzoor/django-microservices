from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer
import random


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # publish('product_created', serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        product.objects.create(id=serializer.data['id'], title=serializer.data['title'], image=serializer.data['image'])
        # publish('product_updated', serializer.data)
        # print(serializer.data)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        # publish('product_deleted', pk)
        print(pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
    def like(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.likes=+1
        product.save()
        resp ={'message':'success'}

        return Response(resp , status=status.HTTP_202_ACCEPTED)    


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        print(users)
        user = random.choice(users)
        return Response({
            'id': user.id
        })