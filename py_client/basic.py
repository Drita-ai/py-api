import requests

endpoint  = "http://127.0.0.1:8000/api/"

op = requests.get(endpoint,params={"abc":123},json={"query":"Hello"})

print(op.text)