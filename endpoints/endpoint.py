

class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Authorization': "bHEAnoXK2Ma1IVo"}
    token = "bHEAnoXK2Ma1IVo"


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
