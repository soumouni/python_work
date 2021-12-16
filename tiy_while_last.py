# try it yourself page 127
#7-8 Deli
sandwish_orders=['novegien','mexicain', 'parisien']
finished_sandwiches=[]

while sandwish_orders:
    for sandwich in sandwish_orders:
        print(f"I made your {sandwich} sandwich")
        finished_sandwiches.append(sandwich)
        sandwish_orders.remove(sandwich)

print("\nThe sandwiches that were made are:\n")
for sandwich in finished_sandwiches:
    print(sandwich.title())
    