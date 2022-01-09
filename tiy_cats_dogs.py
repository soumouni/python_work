# try it yourself page 201
#10-8 Cats and dogs
try:
    with open ('cats.txt') as f: 
        content_f=f.read()        
except FileNotFoundError:
    pass
else:
    print('\ncats.txt contains: ')
    print(content_f)

try:
    with open('dogs.txt') as g: 
        content_g=g.read()        
except FileNotFoundError:
    pass
else:
    print('\ndogs.txt contains: ')
    print(content_g)



