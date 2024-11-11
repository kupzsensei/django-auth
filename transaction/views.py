from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product , Transaction , TransactionItem
from .serializers import ProductSerializer , TransactionSerializer , TransactionPostSerializer
from rest_framework.response import Response
# Create your views here.
class ProductView(APIView):  
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True)
        return Response({'ok': True , 'data': serializer.data})
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok':True , 'data': serializer.data})
        return Response({'ok': False , 'error': serializer.errors})


class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions , many=True)
        return Response({'ok': True , 'data': serializer.data})
    
    def post(self, request):
        serializer = TransactionPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data})
        return Response({'ok': False , 'error': serializer.errors})