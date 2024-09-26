import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer

def api_home(request,*args,**kwargs):

    # Product.object.all().order_by("?") : This creates random query set 
    # and .first() gets the first value
    instance = Product.objects.all().order_by("?").first()

    data = {}

    if instance:
        # fields are the data that i need to add only
        # data = model_to_dict(instance , fields=['id','title','price','sale_price','get_discount'])

        data = ProductSerializer(instance).data

    return JsonResponse(data)