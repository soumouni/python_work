#here we plot the random walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk
mywalk=RandomWalk()
mywalk.fill_walk()

plt.style.use('classic')
fig, ax=plt.subplots(figsize=(15,10))
point_number=range(mywalk.num_points)
    
ax.plot(mywalk.x_values, mywalk.y_values, linewidth=1)
ax.scatter(0,0,c='green', edgecolors='none', s=50)
ax.scatter(mywalk.x_values[-1], mywalk.y_values[-1], c='red', 
edgecolors='none', s=50)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
    