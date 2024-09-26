import json
from django.http import JsonResponse


def api_home(request,*args,**kwargs):

    body = request.body # byte string of JSON DATA
    data = {}

    try:
        data = json.loads(body) # String of JSON data to python Dictionary
    except:
        pass

    print(request.GET) # url query params
    print(data)
    return JsonResponse({"message":"HI, There this is JSON Response"})