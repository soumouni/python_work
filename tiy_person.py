# try it yourself page 99
#6-1 Person
Amel={'first_name':'Amel', 'last_name':'Belhadjoudja', 'Age':43, 
'City':'Algiers'}
print(Amel['first_name'])
print(Amel['last_name'])
print(f"{Amel['Age']} ans")
print(Amel['City'])

#6-2 favorite number
fav_numbers={
    'souad':15,
    'leila':30,
    'hachemi':12,
    'walid':15,
    'moussadegh':5,
    'dalila':3,
}
print(f"\nThe favorite number of Souad is {fav_numbers['souad']} ")
print(f"The favorite number of Leila is {fav_numbers['leila']} ")
print(f"The favorite number of Hachemi is {fav_numbers['hachemi']} ")
print(f"The favorite number of Walid is {fav_numbers['walid']} ")
print(f"The favorite number of Moussadegh is {fav_numbers['moussadegh']} ")
print(f"The favorite number of Dalila is {fav_numbers['dalila']} ")

#6-3 Glossary
glossary={'PEP8':'python enhacement proposal', 'tuple':'list that can not be' 
' modified', 'float':'anynumber with a decimal point', 'append':'add to the'
'end of a list', 'strip':'command that removes blank spaces'}
glossary['dictionary']='list containing pair of key-value'
glossary['loop']='repeating bloc of instructions as many times as needed'
print("\nGLOSSARY:")
for key,value in glossary.items():
    print(f"{key} : {value}")


