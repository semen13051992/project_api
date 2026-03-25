import requests

from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):


    def get_one_meme(self, new_meme):
        self.response = requests.get(f'{self.url}/meme/{new_meme}', headers = self.headers)
        return self.response


    def get_all_memes(self):
        self.response = requests.get(f'{self.url}/meme', headers = self.headers)
        return self.response
