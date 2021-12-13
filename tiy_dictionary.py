#try it yourself page 105
#6-5 Rivers
rivers={'egypt':'nile', 'india':'gange', 'america':'mississipi'}
for key, value in rivers.items():
    print(f"The {value.title()} runs through {key.title()}")

print ("\nthe rivers that are listed in my dictionary are:")
for value in rivers.values():
    print (value.title())

print("\nThe countries listed in my dictionary are:")
for key in rivers.keys():
    print(key.title())

#6-6 favorite language
favorite_language={'souad':'python', 'akram':'java', 'amine':'python', 
'zyad':'scrach'}
target_people=['souad', 'salem', 'nacer', 'selma','amine']
for people in target_people:
    if people in favorite_language.keys():
        print (f"Thank you {people.title()} for taking the poll")
    else:
        print(f"{people.title()} would you please take the poll")
