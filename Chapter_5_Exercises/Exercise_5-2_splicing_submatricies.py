#%%
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

C = np.arange(100).reshape(10,10)
print(C)

print('\n')
C1 = C[0:5,0:5] #C[x,y]

sns.heatmap(C1, cmap='mako', annot=True)


# %%
