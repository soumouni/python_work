#try it yourself page 215
#11-1 City,Country
from tiy_city_function import city_country_formatting

city=input('give me a name of a city: ')
country=input('In whish country is it located: ')
population=input('Please specify the size of its population: ')
info=city_country_formatting(city,country, population)
print(info)