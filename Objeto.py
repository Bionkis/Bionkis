import requests
import json

token = "Bearer <token>"
headers = {"Autorization":token}
r = requests.get('http://google.com',headers = headers)
print(r.status_code)
#json_body = r.json()
