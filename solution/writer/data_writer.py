import json

import requests


class DataWriter:
    @staticmethod
    def write(data):
        headers = {'Content-type': 'application/json'}
        api_endpoint = "https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/query"
        requests.post(url=api_endpoint, data=json.dumps(data), headers=headers)
