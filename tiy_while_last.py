# try it yourself page 127
#7-8 Deli
sandwish_orders=['novegien', 'pastrami','mexicain', 'parisien', 'pastrami',
    'pastrami']
finished_sandwiches=[]

print("The Deli has run out of pastrami\n")
while sandwish_orders:
    for sandwich in sandwish_orders:
        if sandwich == 'pastrami':
            sandwish_orders.remove(sandwich)
        else:
            print(f"I made your {sandwich} sandwich")
            finished_sandwiches.append(sandwich)
            sandwish_orders.remove(sandwich)

print("\nThe sandwiches that were made are:\n")
for sandwich in finished_sandwiches:
    print(sandwich.title())
    
#7-10 Dream vacation
dream_vacations={}
print("this is a poll about friend's dream vacation\n")
while True:
    name=input("Please enter your name ")
    place=input("Where would be you dream vacation ")
    dream_vacations[name]=place
    test=input("Would you like to let another person respond? (Y/N)")
    if test == 'N':
        break
for name, place in dream_vacations.items():
    print(f"\n{name.title()} would love to visite {place.title()}")

