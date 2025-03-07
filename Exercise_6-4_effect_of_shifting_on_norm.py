#%%
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def FrobeniusNorm(A): 
    norm = np.linalg.norm(A, 'fro')
    return norm

A = np.random.randn(20,20)

A_norm = FrobeniusNorm(A)
print(A_norm)

s = np.linspace(0,1,30) # range of scaling parameters (0 to 1 in 30 steps)

# create a list of shifted matricies 
# shift the matrix - remember - The matrix A is added to the scaled idnetity matrix I
shifted_M = []
for i in range(len(s)):
    shifted_M.append(A + s[i]*A_norm*np.eye(20))
    

print(np.shape(shifted_M))
print(shifted_M)


shifted_M_norm = []
percent_change = []
corr_lst = []


for i in range(len(shifted_M)):
    shifted_M_norm.append(FrobeniusNorm(shifted_M[i]))
    percent_change.append((FrobeniusNorm(shifted_M[i])/A_norm)*100)
    
print(shifted_M_norm)

A_norm_lst = [A_norm]*len(shifted_M)
corr, _ = pearsonr(shifted_M_norm, A_norm_lst)
corr_lst.append(float(corr))



#print(len(percent_change))
#print(percent_change)

#print(len(shifted_M_norm))
#print(shifted_M_norm)

fig, axes = plt.subplots(1, 3, figsize=(20,5))


axes[0].plot(s,percent_change,'ko-')
axes[1].plot(s,corr_lst )

    

# %%
