import requests

from endpoints.endpoint  import Endpoint


class TokenVerification(Endpoint):


    def token_verification(self):
        self.response = requests.get(f'{self.url}/authorize/{self.token}')
        return self.response



