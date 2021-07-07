from pprint import pprint
import requests

class YaUploader:
    def __init__(self, file_name: str, disk_file_path: str):
        self.file_name = file_name
        self.disk_file_path = disk_file_path

    def upload(self):
        mytoken = ''
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + mytoken}
        params = {"path": self.disk_file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        #print(response.url)
        pprint(response.json())
        upload_link = response.json()['href']
        #print(upload_link)
        upload_response = requests.put(upload_link, data=open(self.file_name, 'rb'))
        upload_response.raise_for_status()
        if upload_response.status_code == 201:
            return 'Файлы загружены успешно'
        else:
            return ('Ошибка ' + str(upload_response.status_code))


if __name__ == '__main__':
    uploader = YaUploader('file.txt','homework/file.txt')
    print(uploader.upload())