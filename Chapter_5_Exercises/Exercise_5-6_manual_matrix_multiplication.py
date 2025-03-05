#%%
import numpy as np 

m = 4
n = 6
A = np.random.randn(m,n);
B = np.random.randn(n,m)

# build up the product matrix element-wise
C1 = np.zeros((m,m))
for rowi in range(m):
  for coli in range(m):
    C1[rowi,coli] = np.dot( A[rowi,:],B[:,coli] )
    
# implement matrix multiplication directly
C2 = A@B

print(C1)
print(C2)

# compare the results (using isclose(); results should be a matrix of TRUEs)
print(np.isclose( C1,C2 ))
# %%
