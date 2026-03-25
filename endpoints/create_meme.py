import requests

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None


    def create_new_meme(self, body):
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers=self.headers
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.json

