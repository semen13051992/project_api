import requests
import pytest

from utils import *


@pytest.fixture()
def data():
    data = {"info": {"colors": "brown"},
        "tags": ["cat"],
        "text": "TestUser",
        "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"}
    return data


@pytest.mark.parametrize('info', info, 'tags', tags)
def test_create_meme_data( info, tags, data, headers):
    data['info'] = info
    data['tags'] = tags
    response = requests.post(
        'http://memesapi.course.qa-practice.com/meme',
        json=data,
        headers=headers
    )
    assert response.status_code == 200
    json = response.json()
    meme_id = json['id']
    info = json['info']
    tags = json['tags']
    text = json['text']
    url = json['url']

'''
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