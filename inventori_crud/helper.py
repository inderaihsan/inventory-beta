from .models import *
from .serializers import * 

def show_item_list(component_ids) :  
    get_query = Inventory.objects.filter(id__in = component_ids) 
    serialized_value = InventorySerializer(get_query, many = True).data   
    return serialized_value