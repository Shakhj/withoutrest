import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINTS='cbvresponse/'
response=requests.get(BASE_URL+ENDPOINTS)
print(response)
data=response.json()
print(data)