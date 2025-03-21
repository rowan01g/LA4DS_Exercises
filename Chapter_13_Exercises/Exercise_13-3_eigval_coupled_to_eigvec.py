#%%
import numpy as np 
'''
#create random-integer symmetric matrix using additive method: 
N = 5 
A = np.random.randn(N,N)
AtA = (A + A.T)/2

#Diagonilising the matrix (V^-1 LAMBDA V)

l, V = np.linalg.eig(AtA)
L = np.diag(l)

A_recon = V@A@V.T


print(A)
print(A_recon)

check = np.isclose(A, A_recon)
print(check)
print(np.all(check))
'''
# instructions don't specify matrix size; I'll use n=5
N = 5

# to store the reconstruction accuracies
reconAcc = np.zeros(4)


# Create a symmetric random-integers matrix
A = np.random.randn(N,N)
A = np.round( A.T+A )

# diagonalize the matrix
d,V  = np.linalg.eig(A)
D    = np.diag(d)

# demonstrate reconstruction accuracy
# remember that inv(V)=V.T!
Arecon = V @ D @ V.T

check = np.isclose(Arecon, A)
print(check)
     

# %%
