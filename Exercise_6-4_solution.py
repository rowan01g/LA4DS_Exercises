#%%
import matplotlib.pyplot as plt
import numpy as np 

def FrobeniusDistance(A,B): 
    M = A - B
    frob_dis = (np.sum(M**2))
    return frob_dis

# size of the matrix
N = 10

shifting = np.linspace(0,1,30) # 

# original matrix
A = np.random.randn(N,N)
normA = np.linalg.norm(A,'fro')

# initialize results matrices
shiftingResults = np.zeros( (len(shifting),3) )
resultsNames = [ 'Change in norm (%)','Corr. with original','Frobenius distance' ]



for si in range(len(shifting)):

  # shift the matrix - remember - The matrix A is added to the scaled idnetity matrix I
  As = A + shifting[si]*normA*np.eye(N) #Return a 2-D array with ones on the diagonal and zeros elsewhere.

  # get the new norm and transform to %-change
  normShift = np.linalg.norm(As,'fro')
  shiftingResults[si,0] = 100 * (normShift-normA)/normA

  # compute correlation
  shiftingResults[si,1] = np.corrcoef(A.flatten(),As.flatten())[0,1]

  # Frobenius distance
  shiftingResults[si,2] = FrobeniusDistance(A,As)




## plotting!
_,axs = plt.subplots(1,3,figsize=(12,4))

for i in range(3):

  # plot the results
  axs[i].plot(shifting,shiftingResults[:,i],'ks-')
  axs[i].set_xlabel('Shifting (prop. of norm)')
  axs[i].set_ylabel(resultsNames[i])

plt.tight_layout()
plt.savefig('Figure_06_06.png',dpi=300)
plt.show()

# %%
