#%%
import numpy as np 

A = np.random.randn(5,5)
A = A.T@A
Ai = np.linalg.inv(A)


# eigenvalues of A and Ai
eigvals_A  = np.linalg.eig(A)[0]
eigvals_Ai = np.linalg.eig(Ai)[0]

eigvec_A = np.linalg.eig(A)[1]
eigvec_Ai = np.linalg.eig(Ai)[1]

# compare them (hint: sorting helps!)
print('Eigenvalues of A:')
print(np.sort(eigvals_A))

print(' ')
print('Eigenvalues of inv(A):')
print(np.sort(eigvals_Ai))

print(' ')
print('Reciprocal of evals of inv(A):')
print(np.sort(1/eigvals_Ai))

#The eigen vectors for the matrix A and A_inverse are the same, however the elements are found in different positions within the matrix
print(' ')
print('Eigenvectors of A:')
print(np.sort(eigvec_A))

print(' ')
print('Eigenvectors of inv(A):')
print(np.sort(eigvec_Ai))



# %%
