#try it yourself page 315
#plotting the first 500 cubic numbers
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
x=range(-500, 500)
y=[x**3 for x in x]
ax.scatter(x, y, c=y, cmap=plt.cm.Spectral ,s=10)
ax.set_title("cubic numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("cubic value", fontsize=14)

plt.show()
