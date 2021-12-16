#try it yourself page 123
#7-4 pizza topping

prompt="please enter the toppings that you want to add to your pizza"
prompt+="\n\tenter 'quit when you finish \n"

message=''
toppings=[]
while message != 'quit':
    message =input(prompt)
    if message != 'quit':
        toppings.append(message.lower())
        print(f"\t you will add {message.title()} to your pizza")
if message =='quit':
    print('\nThank you for your order, here are the toppings that you ordered')
    for topping in toppings:
        print (topping)
    
#7-5 Movie tickets
n= input("\n\nplease enter how many tickets you would like")
n=int(n)
i=1

while i<=n:
    print(f"Ticket {i}")
    age=input(f"\nhow old is ticket's {i} owner ")
    age=int(age)
    if age < 3:
        print("\nThis ticket is free")
    elif age < 12:
        print("\nYour ticket cost 10$")
    else:
        print ("\nYour ticket cost 15$")
    i+=1
print("\n\t\tEnjoy your movie")

#infinite loop
while True:
    print ("I won't stop printing")
    print ("\n\tPress Ctrl+C if you want to stop this loop")
    break


