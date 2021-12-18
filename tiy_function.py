# try it yourself page 131
#8-1 message
def display_message():
    print ("In this chapter, I am learning how to use functions\n")

print("my message is:")
display_message()

#8-2 favorite book
def favorite_book (title , author='laurent gounelle'):
    print(f"one of my favorite book is: '{title.title()}'")
    print(f"it is written by {author.upper()}\n")

favorite_book(title="le jour ou j'ai appris a vivre", author="shahrour")

#8-3 T-shirt
def make_shirt(size="large", text="'I love python'"):
    print(f"the size of your T-shirt is {size} and it will be customized with "
        f"{text.title()}\n")
print("------call with positional arguments------")
make_shirt('M', "la famille madrigal")

print("------call with keyword arguments------")
make_shirt(text='mountains are calling', size=38)

#8-4 large shirts
#modify 8-3 with default values for both parameters
print("using default values")
make_shirt()
make_shirt(size='medium')
make_shirt(size="small", text="'I love programming'")

#8-5 cities
def describe_city(name_city, country='algeria'):
    print(f"{name_city.title()} is in {country.upper()}\n")
print("\nHere 4 cities:")
describe_city('algiers')
describe_city(name_city='Oran')
describe_city(name_city='paris', country='france')
describe_city('london', 'england')