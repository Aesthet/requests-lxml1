import requests as req
import urllib.parse
import json

_URL_BASE = 'http://petstore.swagger.io/'
_URL_PET = urllib.parse.urljoin(_URL_BASE, '/v2/pet', allow_fragments=True)
_URL_PET_FIND = urllib.parse.urljoin(_URL_BASE, '/v2/pet/findByStatus')


def create_new_pet(pet):
    pet = json.dumps(pet)
    # pet = {
    #     "id": 5, "category": {"id": 5, "name": "string"}, "name": "dogshit", "photoUrls": ["string"],
    #     "tags": [{"id": 5, "name": "string"}], "status": "available",
    # }
    headers = {
        "Accept": "application/xml",
        "Content-Type": "application/json"
    }
    r = req.post(_URL_PET, headers=headers, json=pet)
    print(r.headers)
    print(r.content)
    print(r.status_code)

create_new_pet()
