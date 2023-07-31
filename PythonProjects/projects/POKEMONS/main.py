import requests

token = '8ab4413e905b468054b2b373ed06c78a'
host ='https://api.pokemonbattle.me:9104'
#Создание покемона
response_create=requests.post('https://api.pokemonbattle.me:9104/pokemons',json ={ 
    "name": "Бульба",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"},headers = {'trainer_token': token,'Content-Type':'application/json' })

print(response.text)

#Переименование покемона
response_change_name=requests.put(f'{host}/pokemons',json ={ 
   "pokemon_id":"5615",
    "name":"БульбаЗина",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"},headers = {'trainer_token':token,'Content-Type':'application/json' })

print(response_change_name.text)

#Ловим покемона в покебол
response_catch_poke=requests.post(f'{host}/trainers/add_pokeball',json ={ 
   "pokemon_id":"5615"
    },headers = {'trainer_token': token,'Content-Type':'application/json' })
print(response_catch_poke.text)