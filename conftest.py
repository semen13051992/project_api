import pytest

from endpoints.token_verification import TokenVerification
from endpoints.get_meme import GetMeme
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.update_meme import UpdateMeme


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

@pytest.fixture()
def new_meme(create_meme_endpoint, delete_meme_endpoint):
    body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
            "tags": ["fun","yoda"],
            "text": "Only just begun the meme war has",
            "url": "https://images.theconversation.com/files/177834/original/"
                "file-20170712-14488-19lw3sc.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=926&fit=clip"}
    create_meme_endpoint.create_new_meme(body)
    yield create_meme_endpoint.meme_id
    delete_meme_endpoint.delete_meme(create_meme_endpoint.meme_id)
