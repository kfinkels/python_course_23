import json
import random
import string

import requests


def test_add_pet():
    url = 'http://localhost:8080/pets'

    headers = {'Content-Type': 'application/json'}

    random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    payload = {
        'animal_type': 'Cat',
        'name': random_name
    }

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    # Validate status code and body contents.
    assert resp.status_code == 201
    resp_body = json.loads(resp.text)
    assert resp_body['id'] > 1
    assert resp_body['animal_type'] == 'Cat'
