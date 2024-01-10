import json
import os
import random
import string

from fastapi.testclient import TestClient

from pet_store.main import app


class TestPetStore:

    def setup_class(cls):
        cls.client = TestClient(app)
        cls.random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    def test_add_pet(self):
        headers = {'Content-Type': 'application/json'}
        payload = {
            'animal_type': 'Cat',
            'name': self.random_name
        }

        # convert dict to json by json.dumps() for body data.
        response = self.client.post("/pets", headers=headers, data=json.dumps(payload))

        # Validate status code and body contents.
        assert response.status_code == 200
        resp_body = json.loads(response.text)
        assert resp_body['id'] == 1
        assert resp_body['animal_type'] == 'Cat'

    def test_get_pets(self):
        response = self.client.get("/pets")
        assert response.status_code == 200
        pet = response.json()[0]
        pet.pop('created')
        assert pet == {
            'id': 1,
            'animal_type': 'Cat',
            'name': self.random_name
        }

    def teardown_class(cls):
        os.remove(f"{os.path.abspath(os.curdir)}/pet_store.db")
