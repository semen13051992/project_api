import pytest

#Решил поэксперементировать и сделать генеротор, но не понял как его ограничить

infos = ({"colors": "brown"},{"colors": ["green", "black", "white"]}, {"objects": ["picture", "text"]},
             {'mem': "Dangerous Henry"},{'brand': ['toyota', 'bmw']})

tags = (["cat", "dog"],['cat'],['dog'],['cat', "dog", 'mous','birds'], ['mous', 'birds'])

texts = ('text', 'Instead of a thousand words', 'how and why', 'dominance', 'There are doubts')

urls = ("https://images.meme-arsenal.com/eca8012efce4a5544e7db14553ea15bc.jpg",
    'https://i.pinimg.com/originals/e6/5f/46/e65f46f37e50edecbde4d1a4a4b5b91e.jpg',
    'https://i.pinimg.com/originals/52/77/73/527773378fe2bc1af6378641fbcf618f.jpg?nii=t',
    'https://i.pinimg.com/474x/cd/b7/fe/cdb7fe69d840fbf944ee223f03265e00.jpg?nii=t',
    'https://avatars.mds.yandex.net/i?id=0aaa3088d017b07de75104c3bec81e62_l-4578697-images-thumbs&n=13')


def dates():
    data = {}
    a = 0
    while a <= 100:
        for info in infos:
            for tag in tags:
                for text in texts:
                    for url in urls:
                        data["info"] = info
                        data["tags"] = tag
                        data["text"] = text
                        data["url"] = url
                        #print(data)
                        a += 1
                        yield data


@pytest.mark.parametrize('data', dates())
def test_update_meme_(update_meme_endpoint, new_meme, data):
    body = {
        "id": new_meme,
        "info": data['info'],
        "tags": data['tags'],
        "text": data['text'],
        "url": data['url']}
    update_meme_endpoint.update_put_meme(new_meme, body)
    update_meme_endpoint.check_that_status_is_200()





