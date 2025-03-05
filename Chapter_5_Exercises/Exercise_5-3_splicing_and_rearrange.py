#%%
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

C = np.arange(100).reshape(10,10)
C1 = C[0:5,0:5] #C[Y,X]
C2 = C[0:5,5:10]
C3 = C[5:10, 0:5]
C4 = C[5:10,5:10]

M = np.zeros(100).reshape(10,10)
M[5:10,5:10],M[5:10,0:5],M[0:5,5:10],M[0:5,0:5] = C1,C2,C3,C4

fig, axes = plt.subplots(1, 3, figsize=(20,5))

vmin=0
vmax=100

C_hm = sns.heatmap(data=C, ax=axes[0], cmap='mako', annot=True, vmin=vmin, vmax=vmax)
C1_hm = sns.heatmap(data=C1, ax = axes[1], cmap='mako', annot=True, vmin=vmin, vmax=vmax)
C2_hm = sns.heatmap(data=M, ax = axes[2], cmap='mako', annot=True, vmin=vmin, vmax=vmax)

plt.show()


# %%
