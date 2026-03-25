import pytest

meme_id = [1, 5, 22, 72, 89, 111]

meme_id_negativ = [0, -34, "12!@#$%", "qwerty", 1234567890, 123456789012345678901234567890]

data = [
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "brown"},
    "tags": ["cat"],
    "text": "TestUser",
    "url": "https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg"}]

data_negativ = [
    {"tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text": "Sponge Bob"},
    {"info": 123,
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": 123,
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text": 123,
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": 123},
    {"info": {"12!@#$%^&*()": "green"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "12!@#$%^&*()"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": "12!@#$%^&*()",
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["12!@#$%^&*()"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": "12!@#$%^&*()",
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text": "12!@#$%^&*()",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "12!@#$%^&*()"},
    {"info": {"colors":
        "colors colors colors colors colors colors colors colors colors colors colors colors colors colors colors"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags":
        ["colors colors colors colors colors colors colors colors colors colors colors colors colors colors colors"],
        "text": "Sponge Bob",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text":
        "colors colors colors colors colors colors colors colors colors colors colors colors colors colors colors",
        "url": "www.example.com"},
    {"info": {"colors": "green"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url":
        "colors colors colors colors colors colors colors colors colors colors colors colors colors colors colors"},
{   "info": {"colors colors colors colors colors colors colors colors colors colors colors colors colors colors colors":
        "green"},
        "tags": ["Some tag"],
        "text": "Sponge Bob",
        "url": "www.example.com"}]


def test_token_verification(token_verification_endpoint):
    token_verification_endpoint.token_verification()
    token_verification_endpoint.check_that_status_is_200()


def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_that_status_is_200()


def test_get_one_meme(get_meme_endpoint, new_meme):
    get_meme_endpoint.get_one_meme(new_meme)
    get_meme_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('data', meme_id)
def test_get_meme(get_meme_endpoint, data):
    get_meme_endpoint.get_one_meme(data)
    get_meme_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('data', meme_id_negativ)
def test_get_one_meme_negativ(get_meme_endpoint, data):
    get_meme_endpoint.get_one_meme(data)
    get_meme_endpoint.check_that_status_is_404()


@pytest.mark.parametrize('data', data)
def test_create_meme_data(create_meme_endpoint, data):
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_url_is_correct(data['url'])
    create_meme_endpoint.check_response_info_is_correct(data['info'])
    create_meme_endpoint.check_response_tags_is_correct(data['tags'])
    create_meme_endpoint.check_response_text_is_correct(data['text'])


@pytest.mark.parametrize('data', data_negativ)
def test_create_meme_data_negativ(create_meme_endpoint, data):
    create_meme_endpoint.create_new_meme(data)
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('data', data)
def test_update_meme(update_meme_endpoint, new_meme, data):
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_200()
    #update_meme_endpoint.check_response_id_is_correct(body['id'])
    update_meme_endpoint.check_response_url_is_correct(body['url'])
    update_meme_endpoint.check_response_info_is_correct(body['info'])
    update_meme_endpoint.check_response_tags_is_correct(body['tags'])
    update_meme_endpoint.check_response_text_is_correct(body['text'])


@pytest.mark.parametrize('data', data_negativ)
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


@pytest.mark.parametrize('data', meme_id_negativ)
def test_delete_meme_negativ(delete_meme_endpoint, data):
    delete_meme_endpoint.delete_meme(data)
    delete_meme_endpoint.check_that_status_is_404()
