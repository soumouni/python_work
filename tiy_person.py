# try it yourself page 99
#6-1 Person
Amel={'first_name':'Amel', 'last_name':'Belhadjoudja', 'Age':43, 
'City':'Algiers'}
print(Amel['first_name'])
print(Amel['last_name'])
print(f"{Amel['Age']} ans")
print(Amel['City'])

#6-2 favorite number
#modified according to 6-10
fav_numbers={
    'souad':[15,6,1984],
    'leila':[30,8,1977],
    'hachemi':[12,1979],
    'walid':[15,10,1990],
    'moussadegh':[5,10,1951],
    'dalila':[3,10,1954],
}
for name, numbers in fav_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for numb in numbers:
        print(numb)

#6-3 Glossary
glossary={'PEP8':'python enhacement proposal', 'tuple':'list that can not be' 
' modified', 'float':'anynumber with a decimal point', 'append':'add to the'
'end of a list', 'strip':'command that removes blank spaces'}
glossary['dictionary']='list containing pair of key-value'
glossary['loop']='repeating bloc of instructions as many times as needed'
print("\nGLOSSARY:")
for key,value in glossary.items():
    print(f"{key} : {value}")


