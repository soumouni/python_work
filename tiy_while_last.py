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
    

