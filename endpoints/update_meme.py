import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):


    def update_put_meme(self, new_meme, data):
        self.response = requests.put(
            f'{self.url}/meme/{new_meme}',
            json = data,
            headers = self.headers
        )
        self.json = self.response.json()
        return self.response
