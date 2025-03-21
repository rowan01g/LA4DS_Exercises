#%%

import matplotlib.pyplot as plt
import numpy as np 

# here, r < min{M,N} and the rank of the multiplied matricies is equal to r 
# this produces a reduced rank matrix - there are 15 linearly independant columns in a 30x20 matrix
def rank1():
    M = 30
    N = 20 
    r = 15

    m1 = np.random.randn(M,r)
    m2 = np.random.randn(r,N)

    m1m2 = m1@m2

    print(f'The rank of the matrix m1m2 is: {np.linalg.matrix_rank(m1m2)} and "r" is {r}')
    print(f'However, the shape of the matrix is: {np.shape(m1m2)}')

# r > min{M,N} r is greater than M and N 
# what happens here is that, when r is greater than M and N, the rank becomes equal to N
def rank2(): 
    M = 30
    N = 22 
    r = 40

    m1 = np.random.randn(M,r)
    m2 = np.random.randn(r,N)

    m1m2 = m1@m2

    print(f'The rank of the matrix m1m2 is: {np.linalg.matrix_rank(m1m2)} and "r" is: {r}')
    print(f'However, the shape of the matrix is: {np.shape(m1m2)}')


rank1()
rank2()

#%%
