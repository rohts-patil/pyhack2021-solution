import requests


class DataReader:

    @staticmethod
    def read_subject_list(data_type):
        response = requests.get(
            'https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com//api/1/StudyHack/{data_type}/subject/list'.format(
                data_type=data_type))

        return response.json()['data']

    @staticmethod
    def read_data_for_subject(data_type, subject_id):
        response = requests.get(
            'https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com//api/1/StudyHack/{data_type}/subject/{subject_id}/list'.format(
                data_type=data_type, subject_id=subject_id))

        return response.json()['data']
