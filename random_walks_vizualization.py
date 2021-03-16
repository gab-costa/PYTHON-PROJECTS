import matplotlib.pyplot as plt
from random_walks import RandomWalk
rw=RandomWalk()
rw.fill_walk()
plt.style.use('dark_background')
fig, ax= plt.subplots(figsize=(15,9), dpi=128)
point_numbers= range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)


'''
rw2=RandomWalk()
rw2.fill_walk()

fig2, ax2=plt.subplots()
ax2.scatter(rw2.x_values, rw2.y_values, s=10)
'''
plt.show()