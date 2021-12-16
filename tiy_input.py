# try it yourserlf page 117
#7-1 Rental car
car=input("Which car would you like to rent: ")
print(f"Let me check if I can find you a {car}")

#7-2 Restaurant seating
dinner=input("would you please enter how many people are in your dinner group: ")
dinner=int(dinner)
if dinner > 8 :
    print("I am sorry you will have to wait for a table")
else:
    print("your table is ready")

#7-3 Multiple of ten
number=input("would you please enter a number: ")
number=int(number)
if number % 10 == 0:
    print("this number is a multiple of 10")
else:
    print("this number is not a multiple of 10")