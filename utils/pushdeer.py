import requests


class Pushdeer:
    _url = "http://121.5.73.20:8008/message/push"
    _pushkey = "PDU1T0XQ6yLZtwoc9OYd8ZKcc7w6CmhTH90rb"

    @staticmethod
    def push_msg(text: str, typee: str = "markdown") -> str:
        response = requests.post(url=Pushdeer._url, data={"pushkey": Pushdeer._pushkey, "text": text, "type": typee})
        return response.json()

    @staticmethod
    def pushdeer_img(img_path) -> str:
        img_url = upload_img_to_lsky(img_path)
        return Pushdeer.push_msg(img_url, "image")


def upload_img_to_lsky(img_path):
    url = "http://121.5.73.20:8009/api/v1/upload"
    token = "3|2RNwbysmOafDLrC63uf2cuJ8jwInU5hZtzo1jfM9"
    response = requests.post(url, files={"file": open(img_path, 'rb')},
                             headers={"Authorization": "Bearer " + token,
                                      "Accept": "application/json"})
    img_url = response.json().get("data").get("links").get("url")
    return img_url
