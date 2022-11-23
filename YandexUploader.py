import requests


class YaUploader:
    base_host = "https://cloud-api.yandex.net/"

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def _get_upload_link(self, name):
        uri = "v1/disk/resources/upload/"
        params = {"path": name, "overwrite": True}
        response = requests.get(self.base_host + uri, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']


    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_name = file_path.split("\\")[-1]
        uploader_url = self._get_upload_link(file_name)
        with open(file_path, "rb") as file:
            response = requests.put(uploader_url, data=file, headers=self.get_headers())
        if response.status_code == 201:
            print("Файл загружен")


if __name__ == '__main__':
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)