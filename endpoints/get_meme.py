import requests

from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):


    def get_one_meme(self, new_meme, headers):
        self.response = requests.get(f'{self.url}/meme/{new_meme}', headers = headers)
        return self.response


    def get_all_memes(self, headers):
        self.response = requests.get(f'{self.url}/meme', headers = headers)
        return self.response
