import pytest

from conftest import data_t
from conftest import data_negativ
from conftest import info
from conftest import info_negativ
from conftest import tags
from conftest import tags_negativ
from conftest import text
from conftest import text_negativ
from conftest import url
from conftest import url_negativ
from conftest import meme_id
from conftest import meme_id_negativ

data = {"info": {"colors": "brown"},
        "tags": ["cat"],
        "text": "TestUser",
        "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"}

def test_token_verification(token_verification_endpoint):
    token_verification_endpoint.token_verification()
    token_verification_endpoint.check_that_status_is_200()


def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_that_status_is_200()


def test_get_one_meme(get_meme_endpoint, new_meme):
    get_meme_endpoint.get_one_meme(new_meme)
    get_meme_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('id', meme_id())
def test_get_meme(get_meme_endpoint, id):
    get_meme_endpoint.get_one_meme(id)
    get_meme_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('id', meme_id_negativ())
def test_get_one_meme_negativ_id(get_meme_endpoint, id):
    get_meme_endpoint.get_one_meme(id)
    get_meme_endpoint.check_that_status_is_404()


@pytest.mark.parametrize('data', data_t())
def test_create_meme(create_meme_endpoint, data):
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('data', data_negativ())
def test_create_meme_negativ(create_meme_endpoint, data):
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('info', info())
def test_create_meme_data_info_correct(create_meme_endpoint, info):
    data['info'] = info
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_info_is_correct(data['info'])


@pytest.mark.parametrize('info', info_negativ())
def test_create_meme_data_info_negativ(create_meme_endpoint, info):
    data['info'] = info
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('tags', tags())
def test_create_meme_data_tags_correct(create_meme_endpoint, tags):
    data['tags'] = tags
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_tags_is_correct(data['tags'])


@pytest.mark.parametrize('tags', tags_negativ())
def test_create_meme_data_tags_negativ(create_meme_endpoint, tags):
    data['tags'] = tags
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('text', text())
def test_create_meme_data_text_correct(create_meme_endpoint, text):
    data['text'] = text
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_text_is_correct(data['text'])


@pytest.mark.parametrize('text', text_negativ())
def test_create_meme_data_text_negativ(create_meme_endpoint, text):
    data['text'] = text
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('url', url())
def test_create_meme_data_url_correct(create_meme_endpoint, url):
    data['url'] = url
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_url_is_correct(data['url'])


@pytest.mark.parametrize('url', url_negativ())
def test_create_meme_data_url_negative(create_meme_endpoint, url):
    data['url'] = url
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('data', data_t())
def test_update_meme_(update_meme_endpoint, new_meme, data):
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_200()

@pytest.mark.parametrize('info', info())
def test_update_meme_info_correct(update_meme_endpoint, new_meme, info):
    data['info'] = info
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_response_info_is_correct(body['info'])


@pytest.mark.parametrize('info', info_negativ())
def test_update_meme_info_negativ(update_meme_endpoint, new_meme, info):
    data['info'] = info
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('tags', tags())
def test_update_meme_tags_correct(update_meme_endpoint, new_meme, tags):
    data['tags'] = tags
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_response_tags_is_correct(body['tags'])


@pytest.mark.parametrize('tags', tags_negativ())
def test_update_meme_tags_negativ(update_meme_endpoint, new_meme, tags):
    data['tags'] = tags
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('text', text())
def test_update_meme_text_correct(update_meme_endpoint, new_meme, text):
    data['text'] = text
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_response_text_is_correct(body['text'])


@pytest.mark.parametrize('text', text_negativ())
def test_update_meme_url_negativ(update_meme_endpoint, new_meme, text):
    data['text'] = text
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('url', url())
def test_update_meme_url_correct(update_meme_endpoint, new_meme, url):
    data['url'] = url
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_response_url_is_correct(body['url'])


@pytest.mark.parametrize('text', url_negativ())
def test_update_meme_url_negativ(update_meme_endpoint, new_meme, text):
    data['text'] = text
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('data', data_negativ())
def test_update_meme_data_negativ(update_meme_endpoint, new_meme, data):
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_400()


def test_delete_meme(delete_meme_endpoint, get_meme_endpoint, new_meme):
    delete_meme_endpoint.delete_meme(new_meme)
    delete_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.get_one_meme(new_meme)
    get_meme_endpoint.check_that_status_is_404()


@pytest.mark.parametrize('id', meme_id_negativ())
def test_delete_id_negativ(delete_meme_endpoint, id):
    delete_meme_endpoint.delete_meme(id)
    delete_meme_endpoint.check_that_status_is_404()
