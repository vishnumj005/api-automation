import requests


def get_request_service(url, headers=None, params=None):
    response = requests.get(url=url, headers=headers, params=params)
    return response
