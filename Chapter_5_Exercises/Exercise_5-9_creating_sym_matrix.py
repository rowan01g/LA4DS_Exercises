#%%
import numpy as np 

def isMatrixSymmetric(M):

    Mt = np.transpose(M)
    Mt_check = np.isclose(M, Mt)
    print(np.all(Mt_check))

A = np.random.randn(4,4)
AtA = (A + A.T)/2 # This is the additive method of creating a symmetirc matrix, from a square but nonsymmetic matrix

isMatrixSymmetric(A)
isMatrixSymmetric(AtA)
# %%
