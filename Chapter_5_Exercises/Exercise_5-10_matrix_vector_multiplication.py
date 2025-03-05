#%%
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from numpy import random

# As a matrix with two columns in R3, instead of two separate vectors
A = np.array( [ [3,0],
                [5,2],
                [1,2] ] )

xlim = [-4,4]
scalars = np.random.uniform(low=xlim[0],high=xlim[1],size=(100,2))
print(scalars)

# create random points
points = np.zeros((100,3))
for i in range(len(scalars)):
  points[i,:] = A@scalars[i]

# draw the dots in the figure
fig = go.Figure( data=[go.Scatter3d(x=points[:,0], y=points[:,1], z=points[:,2], mode='markers')])
fig.show()
# %%
