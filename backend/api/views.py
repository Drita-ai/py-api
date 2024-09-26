import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product

def api_home(request,*args,**kwargs):

    # Product.object.all().order_by("?") : This creates random query set 
    # and .first() gets the first value
    model_data = Product.objects.all().order_by("?").first()

    data = {}

    if model_data:
        # fields are the data that i need to add only
        data = model_to_dict(model_data , fields=['id','title','price'])

    return JsonResponse(data)