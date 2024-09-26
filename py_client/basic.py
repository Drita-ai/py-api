import requests

endpoint  = "https://www.github.com"

op = requests.get(endpoint)

print(op.text)