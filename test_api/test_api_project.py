import pytest
from utils import *

def test_token_verification(token_verification_endpoint, authorization_token):
    token_verification_endpoint.token_verification(authorization_token)
    token_verification_endpoint.check_that_status_is_200()


def test_get_all_memes(get_meme_endpoint, headers):
    get_meme_endpoint.get_all_memes(headers)
    get_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.сheck_non_empty_response()


def test_get_one_meme(get_meme_endpoint, new_meme, headers):
    get_meme_endpoint.get_one_meme(new_meme, headers)
    get_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.сheck_non_empty_response()
    get_meme_endpoint.сheck_contents_response()


@pytest.mark.parametrize('id', meme_id)
def test_get_meme(get_meme_endpoint, id, headers):
    get_meme_endpoint.get_one_meme(id, headers)
    get_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.сheck_non_empty_response()
    get_meme_endpoint.сheck_contents_response()


@pytest.mark.parametrize('id', meme_id_negative)
def test_get_one_meme_negative_id(get_meme_endpoint, id, headers):
    get_meme_endpoint.get_one_meme(id, headers)
    get_meme_endpoint.check_that_status_is_404()


@pytest.mark.parametrize('data', data)
def test_create_meme_positive(create_meme_endpoint, get_meme_endpoint, data, headers):
    create_meme_endpoint.create_new_meme(data, headers)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.сheck_non_empty_response()
    create_meme_endpoint.сheck_contents_response()
    create_meme_endpoint.сheck_generated_data(data)
    get_meme_endpoint.get_one_meme(create_meme_endpoint.return_meme_id(), headers)
    get_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.сheck_non_empty_response()
    get_meme_endpoint.сheck_contents_response()
    get_meme_endpoint.сheck_generated_data(data)

@pytest.mark.parametrize('data', data_negative)
def test_create_meme_negative(create_meme_endpoint, data, headers):
    create_meme_endpoint.create_new_meme(data, headers)
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('data', data)
def test_update_meme_data(update_meme_endpoint, new_meme, get_meme_endpoint, data, headers):
    data = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, data, headers)
    update_meme_endpoint.check_that_status_is_200()
    update_meme_endpoint.сheck_non_empty_response()
    update_meme_endpoint.сheck_contents_response()
    update_meme_endpoint.сheck_generated_data(data)
    get_meme_endpoint.get_one_meme(new_meme, headers)
    get_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.сheck_non_empty_response()
    get_meme_endpoint.сheck_contents_response()
    get_meme_endpoint.сheck_generated_data(data)


@pytest.mark.parametrize('data', data_negative)
def test_update_meme_data_negative(update_meme_endpoint, new_meme, get_meme_endpoint, data, headers):
    data = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, data, headers)
    update_meme_endpoint.check_that_status_is_400()


def test_delete_meme(delete_meme_endpoint, get_meme_endpoint, new_meme, headers):
    delete_meme_endpoint.delete_meme(new_meme, headers)
    delete_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.get_one_meme(new_meme, headers)
    get_meme_endpoint.check_that_status_is_404()


@pytest.mark.parametrize('id', meme_id_negative)
def test_delete_id_negativ(delete_meme_endpoint, id, headers):
    delete_meme_endpoint.delete_meme(id, headers)
    delete_meme_endpoint.check_that_status_is_404()
