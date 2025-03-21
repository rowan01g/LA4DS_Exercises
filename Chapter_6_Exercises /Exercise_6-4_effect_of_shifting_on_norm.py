#%%
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def FrobeniusNorm(A): 
    norm = np.linalg.norm(A, 'fro')
    return norm

def FrobeniusDistance(A,B): 
    M = A - B
    frob_dis = (np.sum(M**2))
    return frob_dis

N = 10
A = np.random.randn(N,N)
A_norm = FrobeniusNorm(A)
print(A_norm)

s = np.linspace(0,1,30) # range of scaling parameters (0 to 1 in 30 steps)

# create a list of shifted matricies 
# shift the matrix - remember - The matrix A is added to the scaled idnetity matrix I
shifted_M = []
for i in range(len(s)):
    shifted_M.append(A + s[i]*A_norm*np.eye(N))
    

print(np.shape(shifted_M))
print(shifted_M)


shifted_M_norm = []
percent_change = []
frob_dis = []
corr_lst = []


for i in range(len(shifted_M)):
    shifted_M_norm.append(FrobeniusNorm(shifted_M[i]))
    percent_change.append((FrobeniusNorm(shifted_M[i])/A_norm)*100)
    frob_dis.append(FrobeniusDistance(shifted_M[i], A))


A_norm_lst = [A_norm]*len(shifted_M)
corr, _ = pearsonr(shifted_M_norm, A_norm_lst)
corr_lst.append(float(corr))

print(f'shifted N norm is{shifted_M_norm}')
print(f'A norm list is{A_norm_lst}')
print(f'corr is: {corr}')
print(corr_lst)



#print(len(percent_change))
#print(percent_change)

#print(len(shifted_M_norm))
#print(shifted_M_norm)

fig, axes = plt.subplots(1, 3, figsize=(20,5))


axes[0].plot(s,percent_change,'ko-')
axes[1].plot(s,frob_dis, 'ko-')

    

# %%
