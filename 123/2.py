import requests
import pytest

url = 'http://memesapi.course.qa-practice.com'

def authorization(url):
    body = {"name": "qwerty"}
    response = requests.post(f'{url}/authorize',
        json=body)
    json = response.json()
    token = json['token']
    user = json['user']
    return token

headers = {'Authorization': authorization(url)}

response = requests.get(
        'http://memesapi.course.qa-practice.com/meme',
        headers = headers)
json = response.json()
print(type(json))
print(json['data'][-1])
