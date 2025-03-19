#%%
import numpy as np 
import matplotlib.pyplot as plt

def RandMatrix(): 
    M = input('Please input a value to M to make a MxM matrix')
    r = input('Please input a value for the rank of the matrix, note - if your value of r is greater than M, your matrix rank will be full-rank and equal to M ')

    #if r is less than M, rank of the matrix equals r
    # if r is greater than M, rank of the matrix equals M - (becomes a full rank matrix)

    m1 = np.random.randn(M,r)
    m2 = np.random.randn(r,M)
    m1m2 = m1@m2

    if r < M:
        print(f'Your {M} x {M} matrix has a rank of {np.linalg.matrix_rank(m1m2)}')
    else:
        print(f'Your {M} x {M} matrix is full rank and has a rank of {np.linalg.matrix_rank(m1m2)} - though your selected value of r was {r}')

    return np.linalg.matrix_rank(m1m2)

RandMatrix()