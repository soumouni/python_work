# try it yourself page 181
#9-13 Dice
class Die:
    """this class simulate a die"""
    def __init__(self, sides=6):
        """"initializing attributes of die"""
        self.sides=sides
    
    def roll_die(self):
        """prints a random number between 1 and 6"""
        from random import randint
        n=self.sides
        val=randint(1,n)
        print(val)

die_choice=input("please enter the number of sides your die has: ")
die=Die(int(die_choice))
i=1
while i<=10:
    die.roll_die()
    i+=1

#9-14 Lottery
from random import randint
lottery=[10,15,7,9,6,65,3,5,84,90,'s','w','l','h','m']
j=1
winner=[]
print("the winning combination is: ")
while j<=4:
    m=randint(0,14)
    value=lottery[m]
    print(value)
    j+=1
    winner.append(value)

print(winner)
print("congratulations to the winner")

