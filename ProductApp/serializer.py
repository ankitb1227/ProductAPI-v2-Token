from ProductApp.models import Products
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class Register_List_Serializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'