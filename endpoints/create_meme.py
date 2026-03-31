import requests

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None
    body = {"info": {"colors": "brown"},
     "tags": ["cat"],
     "text": "TestUser",
     "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"}


    def create_new_meme(self, body):
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers=self.headers
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.json

