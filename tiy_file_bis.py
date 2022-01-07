#try it yourself page 193
#10-3 Guest
name=input('please enter your name: ')
with open ('guest.txt', 'w') as file_object:
    file_object.write(name)

#10-4 Guest book
while True:
    prompt='\tplease enter your full name: '
    prompt+='\n\tif you want to quit press q '
    visitor=input(prompt)
    if visitor == 'q':
        break
    else:
        print(f'welcome {visitor.title()}')
        with open ('guest_book.txt','a') as file_object:
            file_object.write(visitor)
            file_object.write('\n')

