import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru"

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets_NO_VALID_KEY_str(self, auth_key, filter):
        headers = {'auth_key': 'abc'}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets_NO_VALID_KEY_int(self, auth_key, filter):
        headers = {'auth_key': '5'}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str):
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
                })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def delete_pet(self, auth_key: json, pet_id: str):
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + '/api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int):
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.put(self.base_url + '/api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: int):

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.post(self.base_url + '/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def add_photo_pet(self, auth_key: json, pet_id: str, pet_photo: str):
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
                })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def post_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.post(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_pet_info(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int):
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.post(self.base_url + '/api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result