import pytest
import requests
from utils import *

url = 'http://memesapi.course.qa-practice.com'

@pytest.fixture()
def body():
    body = {"info": {"colors": "brown"},
         "tags": ["cat"],
        "text": "TestUser",
        "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"}
    return body


@pytest.fixture()
def headers():
    headers = {'Authorization': authorization(url)}
    return headers


def authorization(url):
    body = {"name": "qwerty"}
    response = requests.post(f'{url}/authorize',
        json=body)
    json = response.json()
    token = json['token']
    return token


def test_authorization():
    body = {"name": "qwerty"}
    response = requests.post(f'{url}/authorize',
                             json=body)
    json = response.json()
    token = json['token']
    user = json['user']
    assert response.status_code == 200
    assert response.json()['token'] is not None
    assert response.json()['user'] is not None
    assert response.json()['user'] == 'qwerty'
    assert type(token) is str
    assert type(user) is str


def test():
    response = requests.get(f'{url}/authorize/{authorization(url)}')
    assert response.status_code == 200
    print(response)


def test2(body, headers):
    response = requests.post(
        f'{url}/meme',
        json=body,
        headers=headers
    )
    json = response.json()
    meme_id = json['id']
    assert response.status_code == 200
    assert "id" in json
    assert json['info'] == body['info']
    assert json['tags'] == body['tags']
    assert json['text'] == body['text']
    assert json['url'] == body['url']
    assert len(json) > 0

    response = requests.delete(f'{url}/meme/{meme_id}',
            headers=headers)
    assert response.status_code == 200
    response = requests.get(f'{url}/meme/{meme_id}',
                            headers=headers)
    assert response.status_code == 404



def test3(headers):
    response = requests.get(
        'http://memesapi.course.qa-practice.com/meme/1',
        headers = headers)
    print(response)
    json = response.json()
    meme_id = json['id']
    info = json['info']
    tags = json['tags']
    text = json['text']
    url = json['url']

    assert response.status_code == 200

    assert meme_id is not None
    assert info is not None
    assert tags is not None
    assert text is not None
    assert url is not None

    assert type(json) is dict
    assert type(meme_id) is int
    assert type(info) is dict
    assert type(tags) is list
    assert type(text) is str
    assert type(url) is str

    assert 'id' in json
    assert 'info' in json
    assert 'tags' in json
    assert 'text' in json
    assert 'url' in json

    assert len(json) > 0

#meme_id = [1, 5, 22, 46, 61, 72, 89, 111, 245, 343]

@pytest.mark.parametrize('id', meme_id)
def test4(headers, id):
    response = requests.get(
        f'http://memesapi.course.qa-practice.com/meme/{id}',
        headers = headers)
    print(response)
    json = response.json()
    meme_id = json['id']
    info = json['info']
    tags = json['tags']
    text = json['text']
    url = json['url']

    assert response.status_code == 200

    assert meme_id is not None
    assert info is not None
    assert tags is not None
    assert text is not None
    assert url is not None

    assert type(json) is dict
    assert type(meme_id) is int
    assert type(info) is dict
    assert type(tags) is list
    assert type(text) is str
    assert type(url) is str

    assert 'id' in json
    assert 'info' in json
    assert 'tags' in json
    assert 'text' in json
    assert 'url' in json

    assert len(json) > 0


@pytest.mark.parametrize('info, tags, text, url',
                         [
                             (info,tags, text,url)
                        ]
                         )
def test_create_meme_data( info, tags, text, url, body, headers):
    body['info'] = info
    body['tags'] = tags
    body['text'] = text
    body['url'] = url
    response = requests.post(
        'http://memesapi.course.qa-practice.com/meme',
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    json = response.json()
    meme_id = json['id']
    info = json['info']
    tags = json['tags']
    text = json['text']
    url = json['url']

    assert response.status_code == 200

    assert meme_id is not None
    assert info is not None
    assert tags is not None
    assert text is not None
    assert url is not None

    assert type(json) is dict
    assert type(meme_id) is int
    assert type(info) is dict
    assert type(tags) is list
    assert type(text) is str
    assert type(url) is str

    assert 'id' in json
    assert 'info' in json
    assert 'tags' in json
    assert 'text' in json
    assert 'url' in json

    assert len(json) > 0

    '''
    create_meme_endpoint.check_response_info_is_correct(data['info'])
    create_meme_endpoint.check_response_info_is_correct(data['tags'])
    create_meme_endpoint.check_response_info_is_correct(data['text'])
    create_meme_endpoint.check_response_info_is_correct(data['url'])
    create_meme_endpoint.сheck_non_empty_response()
    create_meme_endpoint.сheck_contents_response()
    create_meme_endpoint.сheck_generated_data(data)
'''


@pytest.mark.parametrize('data', data)
def test_update_meme_data(update_meme_endpoint, new_meme, get_meme_endpoint, data, headers):
    data = {
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.return_meme_id()
    update_meme_endpoint.update_put_meme(data, headers)
    update_meme_endpoint.check_that_status_is_200()
