import pytest
import requests

from endpoints.verification import TokenVerification
from endpoints.get_meme import GetMeme
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.update_meme import UpdateMeme
from endpoints.authorize import Authorization
from endpoints.endpoint import Endpoint


@pytest.fixture()
def data():
    data = {"info": {"colors": "brown"},
        "tags": ["cat"],
        "text": "TestUser",
        "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"}
    return data


@pytest.fixture()
def autorization_endpoint():
    return Authorization()


@pytest.fixture()
def token_verification_endpoint():
    return TokenVerification()


@pytest.fixture()
def get_meme_endpoint():
    return GetMeme()


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


def endpoint_url():
    return Endpoint.url


@pytest.fixture(scope='session')
def authorization_token():
    #url = 'http://memesapi.course.qa-practice.com'
    url = endpoint_url()
    body = {"name": "qwerty"}
    response = requests.post(f'{url}/authorize',
    json=body)
    json = response.json()
    token = json['token']
    #name = json['name']
    return token


@pytest.fixture()
def headers(authorization_token):
    headers = {'Authorization': f'{authorization_token}'}
    return headers


@pytest.fixture()
def new_meme(create_meme_endpoint, delete_meme_endpoint, headers):
    body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
            "tags": ["fun","yoda"],
            "text": "Only just begun the meme war has",
            "url": "https://images.theconversation.com/files/177834/original/"
                "file-20170712-14488-19lw3sc.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=926&fit=clip"}
    create_meme_endpoint.create_new_meme(body, headers)
    yield create_meme_endpoint.meme_id
    delete_meme_endpoint.delete_meme(create_meme_endpoint.meme_id, headers)



