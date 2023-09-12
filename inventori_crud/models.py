from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # is_admin = models.BooleanField(default=False)
    # created_at = models.DateTimeField()
    # created_by = models.CharField(max_length=255, null=True, blank=True)
    # updated_at = models.DateTimeField()
    # updated_by = models.CharField(max_length=255, null=True, blank=True)
    # deleted_at = models.DateTimeField(null=True, blank=True)
    # deleted_by = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta : 
        db_table = 'user'  

class Type(models.Model) : 
    name = models.CharField(max_length = 255) 
    unit = models.CharField(max_length = 255)  
    
    class Meta : 
        db_table = 'type'

class Inventory(models.Model) :
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE) 
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(null = True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True) 
    
    class Meta : 
        db_table = 'inventory' 

class Product(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField()
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)

    class Meta : 
        db_table = 'product' 

class ProductComponent(models.Model) :
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    number_of_usage = models.IntegerField(blank=True, null=True)
    
    class Meta : 
        db_table = 'product_component'