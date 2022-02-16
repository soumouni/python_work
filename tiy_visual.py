#try it yourself page 331
#15-10 histogram with random walk / plot with die_rolling

import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
from random_walk import RandomWalk
prompt="would like to generate data with :"
prompt+="\na:dice rolling"
prompt+="\nb:random walk"
print(prompt)
choice=input("please choose one option or enter 'q' to quit: ")
if choice == 'a':

    #die rolling
    #visalize the results of rolling two die, 1000 time --> with matplotlib
    my_die=Die()
    my_die_2=Die()
    results=[my_die.roll()+my_die_2.roll() for i in range (1000)]
    max_value=my_die.num_sides + my_die_2.num_sides
    frequencies=[results.count(num) for num in range (2,max_value+1)]

    fi,ax=plt.subplots()
    x_values=list(range(2,max_value+1))
    ax.plot(x_values, frequencies, linewidth=2)
    ax.set_title("die roll 1000times", fontsize=24)
    ax.set_xlabel("die values", fontsize=14)
    ax.set_ylabel("frequency", fontsize=14)

    plt.show()

elif choice == 'b':
    #random walk
    my_walk=RandomWalk()
    my_walk.fill_walk()
    
   
