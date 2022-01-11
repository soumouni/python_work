#try it yourself page 208
#10-11 favorite number
import json

def favorite_number():
    """gets the user's favorite number and stores it in a json file"""
    fav=input('tell me your favorite number and I will remember it: ')
    filename='favoritenumber.json'
    with open (filename, 'w') as f:
        json.dump(fav,f)
    return fav

#favorite_number()
#filename='favoritenumber.json'
#with open (filename) as g:
#    numb=json.load(g)
#    print(f"I know your favorite number! it is {numb}")


