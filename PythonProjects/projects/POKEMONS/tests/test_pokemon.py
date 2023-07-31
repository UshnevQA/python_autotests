import requests
import pytest

token = '8ab4413e905b468054b2b373ed06c78a'
host ='https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers',params={'trainer_id':1337})
    assert response.status_code==200


def test_part_of_body():
    response = requests.get(f'{host}/trainers',params={'trainer_id':1337})
    assert response.json()['trainer_name']== 'Полюс'