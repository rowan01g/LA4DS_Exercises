#%%
import matplotlib.pyplot as plt
import numpy as np

v = np.array([1,2])
w = np.array([4,-6])

x = v+w

a1 = plt.arrow(0, 0, v[0], v[1], head_width=.3,width=.1,color='r',length_includes_head=True)
a2 = plt.arrow(v[0], v[1], w[0], w[1], head_width=.3,width=.1,color='b',length_includes_head=True)
a3 = plt.arrow(0, 0, x[0], x[1], head_width=.3,width=.1,color='g',length_includes_head=True)

plt.grid(linestyle='--',linewidth=.5)
plt.axis('square')
plt.axis([-6,6,-6,6])

plt.style.use('ggplot')
plt.show()

# %%
