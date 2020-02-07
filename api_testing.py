import requests as r
import json
import math
import random

# data = {
#     'car_count': 6
# }

# response = r.put('http://192.168.43.129:8000/api/zone/slot/update/2', data=data)

# print(response.text)
# print(response.status_code)


class APIUpdate:

    def __init__(self):
        self.data = {'car_count': 0}
        self.id = 1
        self.url = 'http://192.168.43.129:8000/api/zone/slot/update/'
        self.hit_number = 0

    def update(self):
        self.id = random.randint(1,3)
        self.data['car_count'] = random.randint(0, 10)
        response = r.put(f'{self.url}{self.id}', data=self.data)
        self.hit_number = self.hit_number + 1
        print(f'HTTP: {response.status_code} - HIT {self.hit_number} - VALUE {self.data["car_count"]}')


api = APIUpdate()

while True:
    api.update()