#%%
import numpy as np 
from scipy.stats import pearsonr
from numpy import dot 
from numpy.linalg import norm

v1 = np.arange(0,4)
#[:, None] turns the single row array into a column array
v2 = np.arange(-50, 51)[:, None]*np.ones((1,4), dtype=int)

#initialise zeros vector to store offset values 
v3 = np.zeros((101,4),dtype=int)
for i in range(len(v2)):
    v3[i] = (v2[i] + v1)
print(f'The first 5 Rows of v3 are:\n{v3[0:6]}')    
    




# %%
