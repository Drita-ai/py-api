import requests

endpoint  = "http://127.0.0.1:8000/api/"

op = requests.post(endpoint,json={"title":"Hello"})

# print(op.json())