import tiy_favorite_number
import json

filename='favoritenumber.json'
try:
    with open (filename) as f:
        fav=json.load(f)
        print(f'I remember your favorite number {fav}')
except FileNotFoundError:
    tiy_favorite_number.favorite_number()
    print('thank you, I will remember your number')