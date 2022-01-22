#here we plot the random walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    mywalk=RandomWalk()
    mywalk.fill_walk()

    plt.style.use('classic')
    fig, ax=plt.subplots()
    point_number=range(mywalk.num_points)
    ax.scatter(mywalk.x_values, mywalk.y_values,c=point_number, 
    cmap=plt.cm.Blues, edgecolors='none', s=15)

    plt.show()
    
    keep = input('do you want to continue y/n ')
    if keep == 'n':
        break