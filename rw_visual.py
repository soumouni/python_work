#here we plot the random walk
from ast import Break
from tkinter import Y
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    mywalk=RandomWalk()
    mywalk.fill_walk()

    plt.style.use('classic')
    fig, ax=plt.subplots()
    ax.scatter(mywalk.x_values, mywalk.y_values,c='red', s=5)
    plt.show()
    keep = input('do you want to continue y/n ')
    if keep == 'n':
        break