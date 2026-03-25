import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    meme_id = None


    def delete_meme(self, meme_id):
        self.meme_id = meme_id
        self.response = requests.delete(f'{self.url}/meme/{meme_id}',
        headers=self.headers)
        return self.response
