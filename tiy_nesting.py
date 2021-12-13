#try it yourself page 112
#6-7 people
#start with 6-1 Person
amel={'first_name':'Amel', 'last_name':'Belhadjoudja', 'Age':43, 
    'City':'Algiers'}
amine={'first_name':'Amine', 'last_name':'Rebbani', 'Age':50, 
    'City':'Algiers'}
lamia={'first_name':'Lamia', 'last_name':'Ouis', 'Age':38, 
    'City':'Algiers'} 
people=[amel, amine, lamia]

for friend in people:
    print(f"\n{friend['first_name']} {friend['last_name']} is: {friend['Age']}"
        f" years old and lives in {friend['City']}.")

#6-8 pets
helly={'name':'helly','pet':'dog', 'owner':'ferroudja'}
flocon={'name':'flocon','pet':'cat','owner':'amel'}
floki={'name':'floki','pet':'dog','owner':'bourouba'}
pets=[helly,flocon,floki]
for pet in pets:
    print(f"{pet['name'].title()} is a {pet['pet']} and it's owner is "
        f"{pet['owner'].upper()}")

#6-9 favorite places
favorite_places={
    'souad':['lisboa', 'djanet', 'canada'],
    'amel':['nigeria','canada'],
    'leila':['barcelona', 'antalya'],
}
for name,value in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in value:
        print (place)

#6-11 cities
cities={
    'lisboa':{'country':'portugal', 'continent':'europe', 'fact':' has amazing' 
        ' seefood'},
    'calgary':{'country':'canada', 'continent':'america','fact':'is very cold'},
    'djanet':{'country':'algeria','continent':'africa', 'fact':'is in the desert'}
}
for city, info in cities.items():
    print(f"the city of {city.title()} is")
    for key, value in info.items():
        print (f"\t{key}: {value}")