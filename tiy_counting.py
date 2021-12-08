#try it yourself of page 60
#counting to 20
for value in range(1,21):
    print(value)

#one hundred
hundred=[value for value in range(1,100)]
print(hundred)
for value in hundred:
    print (value)

#million
#million=[value for value in range(1,1000000)]
#print(million)
#for value in million:
#    print (value)

#min, max and sum
print(f"min= {min(hundred)}")
print(f"max = {max(hundred)}")
print(f"sum(1,100)= {sum(hundred)}")

#list of odd numbers
odds=[value for value in range(1,21,2)]
print(odds)
for value in range(1,21,2):
    print(value)               #printing odd numbers one by one

##Threes
threes=[value*3 for value in range(1,11)]
print(threes)

#Cubes
cubes=[value**3 for value in range(1,11)]
print(f"cubes= {cubes}")