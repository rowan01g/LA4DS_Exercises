#%%
import numpy as np
import matplotlib.pyplot as plt 

def RandMatrix(M,N,r): 
    
    m1 = np.random.randn(M,r)
    m2 = np.random.randn(r,N)
    RandM = m1@m2

    return RandM

#All the following matricies have the same rank
a1 = RandMatrix(20, 20, 15)
print(np.linalg.matrix_rank(a1))
print(np.linalg.matrix_rank(a1.T))
print(np.linalg.matrix_rank(a1.T@a1))
print(np.linalg.matrix_rank(a1@a1.T))

print('\n')

#ranks are same even for wide matricies
a2 = RandMatrix(20, 40, 18)
print(np.linalg.matrix_rank(a2))
print(np.linalg.matrix_rank(a2.T))
print(np.linalg.matrix_rank(a2.T@a2))
print(np.linalg.matrix_rank(a2@a2.T))

print('\n')

#ranks are also the same for tall matricies
a3 = RandMatrix(40, 20, 12)
print(np.linalg.matrix_rank(a3))
print(np.linalg.matrix_rank(a3.T))
print(np.linalg.matrix_rank(a3.T@a3))
print(np.linalg.matrix_rank(a3@a3.T))


# %%
