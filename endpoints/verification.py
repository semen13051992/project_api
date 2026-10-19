import requests

from endpoints.endpoint  import Endpoint

class TokenVerification(Endpoint):


    def token_verification(self,authorization_token):
        self.response = requests.get(f'{self.url}/authorize/{authorization_token}')
        return self.response
