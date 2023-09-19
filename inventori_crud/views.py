from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from . models import * 
from . serializers import * 
from rest_framework import status
from datetime import datetime
# Create your views here.

@api_view(['GET']) 
def hello_world(request) : 
    return Response({'message' : 'Api running'}) 

@api_view(['GET']) 
def view_all_inventory(request) : 
    get_query = Inventory.objects.all()  
    serialized = InventorySerializer(get_query, many = True).data
    return Response({'data' : serialized},status= status.HTTP_200_OK)

@api_view(['GET']) 
def get_inventory_by_id(request, inventory_id) : 
    get_query = Inventory.objects.filter(id = inventory_id) 
    serialized = InventorySerializer(get_query, many = True).data 
    return Response({'data' : serialized, 'message' :'fetched'}, status=status.HTTP_200_OK) 

@api_view(['POST']) 
def create_inventory(request) : 
    name = request.data['name']
    location = request.data['location']
    user_id = request.data['user_id'] 
    type_id = request.data['type_id'] 
    creator = User.objects.get(id = user_id).username
    created_at = datetime.now()
    Inventory.objects.create(name = name, location = location, created_by = creator, created_at = created_at, type_id = type_id) 
    return Response({'data' : [], 'message' : 'inventori kamu berhasil dibuat!'}, status = status.HTTP_200_OK) 

@api_view(['POST']) 
def update_inventory(request) : 
    inventory_id = request.data['inventory_id'] 
    name = request.data['name']
    location = request.data['location']
    user_id = request.data['user_id'] 
    type_id = request.data['type_id']  
    type_obj = Type.objects.get(id = type_id) 
    updated_by = User.objects.get(id = user_id).username
    inventory_obj = Inventory.objects.get(id = inventory_id) 
    inventory_obj.name = name
    inventory_obj.location = location 
    inventory_obj.user = user_id 
    inventory_obj.type = type_obj 
    inventory_obj.updated_by = updated_by 
    inventory_obj.updated_at = datetime.now() 
    inventory_obj.save() 
    return Response({'data' : [], 'message' : 'Inventori kamu berhasil diperbaharui!'}, status = status.HTTP_200_OK) 

@api_view(['POST']) 
def delete_inventory(request) : 
    id = request.data['id'] 
    Inventory.objects.filter(id = id).delete() 
    return Response({'message' : 'data berhasil dihapus'}, status=status.HTTP_200_OK)

#Master TYPE
@api_view(['GET']) 
def view_all_type(request) : 
    get_query = Type.objects.all() 
    serialized = TypeSerializer(get_query, many = True).data 
    return Response({'data' : serialized}, status = status.HTTP_200_OK) 

@api_view(['GET']) 
def get_type_by_id(request, type_id) : 
    get_query = Type.objects.filter(id = type_id) 
    serialized = TypeSerializer(get_query, many = True).data
    return Response({'data' : serialized}, status = status.HTTP_200_OK) 

@api_view(['POST']) 
def create_type(request) : 
    name = request.data['name']
    unit = request.data['unit'] 
    Type.objects.create(name = name, unit = unit) 
    return Response({'message' : 'Spesifikasi tipe berhasil dibuat'}, status = status.HTTP_200_OK) 
 
@api_view(['POST']) 
def delete_type(request) : 
    id = request.data['id']  
    Type.objects.filter(id = id).delete() 
    return Response({'message' : 'deleted'})   

@api_view(['POST']) 
def update_type(request) : 
    id = request.data['id']
    name = request.data['name']
    unit = request.data['unit']
    Type.objects.filter(id = id).update(name = name, unit = unit) 
    return Response({'message' : 'updated!'})     

#Create Component