def verify_status(response, expected_code):
    assert response.status_code == int(expected_code), \
        f'Expected status code:{expected_code},' \
        f' but was: {response.status_code} with body: {response.text} for {response.request.method} {response.url}'
    if response.status_code != int(expected_code):
        print(response)


def get_value(res, key):
    return res.json()[key]


def is_email_exists(res, email):
    for json_data in res.json()['data']:
        if json_data['email'] == email:
            return True

    return False
