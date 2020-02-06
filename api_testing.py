import requests as r
import json

data = {
    'car_count': 2
}

response = r.put('http://localhost:8000/zone/1/update/', data=data)

print(response.text)
print(response.status_code)