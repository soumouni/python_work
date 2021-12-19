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

#8-6 City names
def city_country(city, country):
    """well formatted cit, country string"""
    city_country=f"'{city.title()}, {country.title()}'\n"
    return city_country
pair1=city_country('algiers', 'algeria')
pair2=city_country('paris', 'france')
pair3=city_country('london','england')
print(pair1)
print(pair2)
print(pair3)

#8-7 album
def make_album(artist_name, album_title, number_songs='none'):
    """return a dictionary containing album informations"""
    if number_songs:
        make_album={'artist':artist_name, 'title':album_title, 
        'number_of_songs':number_songs}
    else:
        make_album={'artist':artist_name, 'title':album_title}
    return make_album
first_album=make_album('pink floyd', 'confortably numb')
second_album=make_album('metallica', 'the unforgiven')
third_album=make_album('tinariwen', 'aman')
print(first_album)
print(second_album)
print(third_album)
fourth_album=make_album('cold play', 'yellow', 12)
print(fourth_album)

#8-8 user albums
while True:
    print("please enter album informations: ")
    print("press 'q' if you want to quit")
    artist=input("enter album's artist: ")
    if artist == 'q':
        break
    title=input("enter album's title: ")
    if title == 'q':
        break
    album=make_album(artist, title)
    print(album)

#8-9 Messages
text_messages=['je suis en reunion','je te rappelle', 'sms please']
text_messages +=['je ne peux pas te parler', 'a tte']
def show_message(message_list):
    """displays all messages in the list text_message"""
    for message in message_list:
        print(message)
show_message(text_messages)

#8-10 sending messages
sent_messages=[]

def send_messages(text_messages, sent_messages):
    while text_messages:
        message=text_messages.pop()
        print (f" sending {message} message")
        sent_messages.append(message)

print(f"messages that needs to be sent: {text_messages}")
print(f" sent messages: {sent_messages}")
print("\n after send function")
#send_messages(text_messages, sent_messages)
#print(f"messages that needs to be sent: {text_messages}")
#print(f" sent messages: {sent_messages}")

#8-11 Archived messages
send_messages(text_messages[:], sent_messages)
print(f"messages that needs to be sent: {text_messages}")
print(f" sent messages: {sent_messages}")

#8-12 Sandwiches
def sandwich(*items):
    """print list of elements in the sandwich ordered"""
    print("\nyour sandwich contains:")
    for item in items:
        print(item.title())

sandwich('cheese')
sandwich('tuna', 'cheese')
sandwich ('salmon', 'cheese', 'cucumber')

#8-13 User profile
def user_profile(first_name, last_name, **user_info):
    """return dictionary containing user info"""
    user_info['first_name']=first_name
    user_info['last_name']=last_name
    return user_info
user=user_profile('souad', 'mimouni',age=37,city='algiers', eye_color='brown')
print(user)

#8-14 Cars
def make_cars(manufacturer, model, **car_info):
    """return dictionary with car information"""
    car_info['car_manufacturer']=manufacturer
    car_info['car_model']=model
    return car_info

car=make_cars('chevrolet', 'spark', color='black', AC= True)
print(car)
