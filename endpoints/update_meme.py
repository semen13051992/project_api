import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):


    def update_put_meme(self, meme_id, data, headers):
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json = data,
            headers = headers
        )
        #self.json = self.response.json()
        return self.response
