"""
URL configuration for inventoriku project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("init/", views.hello_world),
    path("items/", views.view_all_inventory),
    path("create-items/", views.create_inventory),
    path("update-items/", views.update_inventory),
    path("get-spesific-items/<str:inventory_id>", views.get_inventory_by_id),
    path("delete-items", views.delete_inventory),
    path("item-type/", views.view_all_type),
    path("get-spesific-item-type/<str:type_id>", views.get_type_by_id),
    path("create-item-type", views.create_type),
    path("update-item-type", views.update_type),
    path("delete-item-type", views.delete_type),
    path("create-product", views.create_product),
    path("product", views.view_all_product), 
    path("create-product-component", views.create_product_component),
    path("product-component", views.view_all_product_component),
    path("product-component/<str:product_id>", views.get_product_component_by_product),
    path('create-purchase', views.purchase_items),
    path('purchase', views.view_all_purchase_items)
    
]
