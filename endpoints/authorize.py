import requests

from endpoints.endpoint  import Endpoint


class Authorization(Endpoint):


    def authorization(self):
        body = {"name": "qwerty"}
        self.response = requests.post(f'{self.url}/authorize',
            json=body)
        self.json = self.response.json()
        self.token = self.json['token']
        self.name = self.json['name']
        return self.token



