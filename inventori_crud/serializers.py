from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = Type
        fields ='__all__' 

class ProductComponentSerializer(serializers.ModelSerializer): 
    inventory = InventorySerializer() 
    product = serializers.SerializerMethodField()
    class Meta : 
        model = ProductComponent
        fields =["inventory", "product", "number_of_usage"]  
        
        
        
class PurchaseSerializer(serializers.ModelSerializer) : 
    inventory = InventorySerializer() 
    class Meta : 
        model = purchase_list 
        fields = '__all__'
        
        
        