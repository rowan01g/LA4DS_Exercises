#%%
import numpy as np 
'''
A = np.random.randn(12).reshape(4,3)
B = np.random.randn(16).reshape(4,4)
v = np.random.randn(4).reshape(4,1)

A_aug = np.hstack((A, v))
B_aug = np.hstack((B, v))

A_rank = np.linalg.matrix_rank(A)
A_aug_rank = np.linalg.matrix_rank(A_aug)
B_rank = np.linalg.matrix_rank(B)
B_aug_rank = np.linalg.matrix_rank(B_aug)

print(A)
print(v)
print(A_aug)
print('\n')

print(A_rank)
print(A_aug_rank)

print('\n')

print(B_rank)
print(B_aug_rank)
'''

#creates a random matrix with dimesnion derived from the arguments
def RandnMatrix(M, N): 
    A = np.random.randn(M*N).reshape(M,N)
    print(f'Your generated matrix is: \n {A}')
    print(f'The rank of your matrix is: {np.linalg.matrix_rank(A)}')
    return A
# Takes a matrix A and vector v 
def inColumnSpace(A, v):
    A_aug = np.hstack((A,v))
    
    A_rank = np.linalg.matrix_rank(A)
    A_aug_rank = np.linalg.matrix_rank(A_aug)

    if A_rank == A_aug_rank:
        print(f'The vector, v, is contained within the column space of the matrix')
    elif A < A_aug_rank:
        print(f'The vector, v, is not contained within the column space of matrix A')
    return A_rank, A_aug_rank

v = np.random.randn(4).reshape(4,1)
A = RandnMatrix(4,4)
inColumnSpace(A, v)

     
    




# %%
