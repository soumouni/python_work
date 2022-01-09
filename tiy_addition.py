#try it yourself page 201
#10-6 Addition
#10-7 addition calculator (adding a loop)
while True:
    print("give me two numbers and I will add them up")
    print("enter 'q' if you want to quit")
    first_number=input('please enter your first number: ')
      
    if (first_number == 'q'):
        break
    else:
        while True:
                try:
                    a=int(first_number)
                except ValueError:
                    print("This input is not accepted, would you please enter "
                    "a valide integer")
                    first_number=input('please enter your valid first number: ')
                else:
                    break 
        second_number=input('please enter your second number: ')
    if (second_number == 'q'):
        break
    else:
        while True:
                try:
                    b=int(second_number)
                except ValueError:
                    print("This input is not accepted, would you please enter "
                    "a valide integer")
                    second_number=input('please enter your valid second number: ')
                else:
                    break 
                       
    c=a+b
    print(f'{a} + {b} = {c}')
    