#%%

import matplotlib.pyplot as plt
import numpy as np 

M = 10
N = 20 
r = 15

m1 = np.random.randn(M,r)
m2 = np.random.randn(r,N)

m1m2 = m1@m2

print(f'The rank of the matrix m1m2 is: {np.linalg.matrix_rank(m1m2)}')
print(np.shape(m1m2))


#%%
