import requests
import json

listnamehero = {"Hulk": 0, "Captain America": 0, "Thanos": 0}
stoken = "2619421814940190"
spage = "search"

for namehero in listnamehero:
    surl = f"https://superheroapi.com/api/{stoken}/{spage}/{namehero}"
    resp = requests.get(surl)
    sjson = json.loads(resp.content)
    listnamehero[namehero] = sjson['results'][0]['powerstats']['intelligence']

print(f"самый умный супергерой: {sorted(listnamehero)[-1]}")

from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        href = self.get_upload_link(file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл загружен")


if __name__ == '__main__':
    token = ""
    uploader = YaUploader(token)
    uploader.upload('1.txt')
