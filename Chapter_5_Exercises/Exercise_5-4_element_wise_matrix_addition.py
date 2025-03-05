#%%
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

xlim=(0,10)


A = np.arange(100).reshape(10,10)
B = np.random.randint(low=xlim[0], high=xlim[1], size=(100,)).reshape(10,10)
C = np.random.randint(low=xlim[0], high=xlim[1], size=(40,)).reshape(5, 8) # mismatching size matrix

sumAB = np.zeros_like(A)
for i in range(len(A)):
    for j in range(len(A[0])):
        sumAB[i][j] = A[i][j]+B[i][j]

#sumAC = np.zeros_like(A)
#for i in range(len(A)):
#    for j in range(len(A[0])):
#        sumAC[i][j] = A[i][j]+C[i][j]

#print(sumAC)

fig, axes = plt.subplots(1, 3, figsize=(20,5))
vmin = 0
vmax = 110

A_hm = sns.heatmap(data=A, ax=axes[0], cmap='mako', annot=True, vmin=vmin, vmax=vmax)
B_hm = sns.heatmap(data=B, ax=axes[1], cmap='mako', annot=True, vmin=vmin, vmax=vmax)
sumAB_hm = sns.heatmap(data=sumAB, ax=axes[2], cmap='mako', annot=True, vmin=vmin, vmax=vmax)

plt.show()

# %%
