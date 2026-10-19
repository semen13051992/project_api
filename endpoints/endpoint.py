import requests


class Endpoint:

    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None


    def check_that_status_is_200(self):
        assert self.response.status_code == 200


    def check_that_status_is_404(self):
        assert self.response.status_code == 404


    def check_that_status_is_400(self):
        assert self.response.status_code == 400


    def check_response_id_is_correct(self, data):
        assert self.json['id'] == data


    def check_response_info_is_correct(self, data):
        assert self.json['info'] == data


    def check_response_tags_is_correct(self, data):
        assert self.json['tags'] == data


    def check_response_text_is_correct(self, data):
        assert self.json['text'] == data


    def check_response_url_is_correct(self, data):
        assert self.json['url'] == data


    def сheck_non_empty_response(self):
        json = self.response.json()
        assert type(json) is dict
        assert len(json) > 0


    def сheck_contents_response(self):
        json = self.response.json()
        assert 'id' in json
        assert 'info' in json
        assert 'tags' in json
        assert 'text' in json
        assert 'url' in json
        meme_id = json['id']
        info = json['info']
        tags = json['tags']
        text = json['text']
        url = json['url']
        assert meme_id is not None
        assert info is not None
        assert tags is not None
        assert text is not None
        assert url is not None
        assert type(json) is dict
        #assert type(meme_id) is int
        assert type(info) is dict
        assert type(tags) is list
        assert type(text) is str
        assert type(url) is str
        print(type(meme_id))


    def сheck_generated_data(self, body):
        json = self.response.json()
        assert "id" in json
        assert json['info'] == body['info']
        assert json['tags'] == body['tags']
        assert json['text'] == body['text']
        assert json['url'] == body['url']


    def return_meme_id(self):
        json = self.response.json()
        return json['id']