import json
from django.http import JsonResponse

from products.models import Product

def api_home(request,*args,**kwargs):

    # Product.object.all().order_by("?") : This creates random query set 
    # and .first() gets the first value
    model_data = Product.objects.all().order_by("?").first()

    data = {}

    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

    return JsonResponse(data)