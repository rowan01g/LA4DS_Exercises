#%%
import numpy as np

xlim=(0,11)
L = np.random.randint(low=xlim[0],high=xlim[1], size = 12).reshape(2,6)
I = np.random.randint(low=xlim[0],high=xlim[1], size = 18).reshape(6,3)
V = np.random.randint(low=xlim[0],high=xlim[1], size = 15).reshape(3,5)
E = np.random.randint(low=xlim[0],high=xlim[1], size = 10).reshape(5,2)

LIVE = np.transpose(L@I@V@E)
EVIL = np.transpose(E)@np.transpose(V)@np.transpose(I)@np.transpose(L)

print(np.isclose(LIVE,EVIL)) # Confirming (LIVE)^T == E^TV^TI^TL^T

# %%
