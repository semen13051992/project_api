import pytest

from endpoints.token_verification import TokenVerification
from endpoints.get_meme import GetMeme
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.update_meme import UpdateMeme


def meme_id():
    meme_id = [1, 5, 22, 46, 61, 72, 89, 111, 245, 343]
    return meme_id

@pytest.fixture()
def data():
    data = {"info": {"colors": "brown"},
        "tags": ["cat"],
        "text": "TestUser",
        "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"}
    return data


def meme_id_negativ():
    meme_id_negativ = [0, -34,"12!@#$%", "qwerty", 12345, 1234567890,12345678901234567890]
    return meme_id_negativ


def info():
    info = [{"colors": "brown"},{"colors": ["green", "black", "white"]}, {"objects": ["picture", "text"]},
        {'mem': "Dangerous Henry"},{'brand': ['toyota', 'bmw']}]
    return info


def info_negativ():
    info = [{"c": "g"}, {"": ""}, {"12!@#$": "12!@#$"}, {123: 123}]
    return info


def tags():
    tags = [["cat", "dog"],['cat'],['dog'],['cat', "dog", 'mous','birds'], ['mous', 'birds']]
    return tags


def tags_negativ():
    tags_negativ = [{"c": "g"}, {"": ""}, {"12!@#$": "12!@#$"}, {123: 123}]
    return tags_negativ


def text():
    text = ['text', 'Instead of a thousand words', 'how and why', 'dominance', 'There are doubts']
    return text


def text_negativ():
    text_negativ = [{"c": "g"}, {"": ""}, {"12!@#$": "12!@#$"}, {123: 123}]
    return text_negativ


def url():
    url = ["https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg",
        'https://i.pinimg.com/originals/e6/5f/46/e65f46f37e50edecbde4d1a4a4b5b91e.jpg',
        'https://i.pinimg.com/originals/52/77/73/527773378fe2bc1af6378641fbcf618f.jpg?nii=t',
        'https://i.pinimg.com/474x/cd/b7/fe/cdb7fe69d840fbf944ee223f03265e00.jpg?nii=t',
        'https://avatars.mds.yandex.net/i?id=0aaa3088d017b07de75104c3bec81e62_l-4578697-images-thumbs&n=13']
    return url


def url_negativ():
    url_negativ = [{"c": "g"}, {"": ""}, {"12!@#$": "12!@#$"}, {123: 123}]
    return url_negativ


def data_t():
    data = [
        {
        "info": {"colors": "brown"},
        "tags": ["cat"],
        "text": "TestUser",
        "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"},
        {
        "info": {"colors": ["green", "black", "white"]},
        "tags": ["cat", "dog"],
        "text": "text",
        "url": "https://i.pinimg.com/originals/e6/5f/46/e65f46f37e50edecbde4d1a4a4b5b91e.jpg"},
        {
        "info": {"objects": ["picture", "text"]},
        "tags": ['dog'],
        "text": "Instead of a thousand words",
        "url": 'https://i.pinimg.com/originals/52/77/73/527773378fe2bc1af6378641fbcf618f.jpg?nii=t'},
        {
        "info": {'mem': "Dangerous Henry"},
        "tags": ['cat', "dog", 'mous','birds'],
        "text": "how and why",
        "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"},
        {
        "info": {'brand': ['toyota', 'bmw']},
        "tags": ['mous', 'birds'],
        "text": "There are doubts",
        "url": "https://avatars.mds.yandex.net/i?id=0aaa3088d017b07de75104c3bec81e62_l-4578697-images-thumbs&n=13"}]
    return data


def data_negativ():
    data_negativ = [
        {
        "info": {"": ""},
        "tags": [""],
        "text": "",
        "url": ""},
        {
        "info": {123: 123},
        "tags": [123],
        "text": 123,
        "url": 123},
        {
        "info": {"12!@#$%": "12!@#$%"},
        "tags": ['12!@#$%'],
        "text": "12!@#$%",
        "url": '12!@#$%'},
        {
        "info": {'q': "e"},
        "tags": ['a'],
        "text": "x",
        "url": "n"},
        {
        "info": {'brandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrandbrand':
                'toyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyotatoyota'},
        "tags": ['birdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirdsbirds'],
        "text": "There are doubts There are doubts There are doubts There are doubts There are doubts There are doubts",
        "url": "https://avatars.mds.yandex.net/i?id=0aaa3088d017b07de75104c3bec81e62_l-4578697-images-thumbs&n=13"}]
    return data_negativ


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
