from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ProductApp.serializer import Register_List_Serializer
from .models import Products

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class Product_Create_List(APIView):
    def post(self, request, *args, **kwargs):
        mydata = request.data
        serialized_data = Register_List_Serializer(data=mydata)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)

    def get(self, request):
        mydata = Products.objects.all()
        serialized_data = Register_List_Serializer(mydata, many=True)
        return Response(serialized_data.data)

class Product_Update(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #
    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)

    def get(self, request, id):
        mydata = Products.objects.filter(id=id)
        if not mydata.exists():
            return Response({"Message": "Id doesn't exists"})
        serialized_data = Register_List_Serializer(mydata.first())
        return Response(serialized_data.data)

    def put(self, request, id):
        product = Products.objects.filter(id=id)
        mydata = request.data
        if not product.exists():
            return Response({"Message": "Id doesn't exists"})
        serialized_data = Register_List_Serializer(data=mydata, instance=product.first())
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)

    def delete(self, request, id):
        product = Products.objects.filter(id=id)
        if not product.exists():
            return Response({"Message": "Id doesn't exists"})
        name = product.first().name
        product.first().delete()
        return Response({'Message': f"The product {name} has been deleted"})

    # def checkId(self, product):
    #     if not product.exists():
    #         return Response({"Message": "Id doesn't exists"})