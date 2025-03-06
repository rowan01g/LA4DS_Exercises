#%%
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def FrobeniusNorm(A): 
    norm = np.linalg.norm(A, 'fro')
    return norm

A = np.random.randn(10,10)

A_norm = FrobeniusNorm(A)
print(A_norm)
D = np.diag(np.full(10,1))
s = np.linspace(0,1,30) # range of scaling parameters (0 to 1 in 30 steps)

# create a list of shifted matricies 
shifted_M = []
for i in range(len(s)):
    I = s[i]*D
    shifted_M.append(A@I)

print(np.shape(shifted_M))
print(shifted_M)

shifted_M_norm = []
percent_change = []
corr_lst = []

for i in range(len(shifted_M)):
    shifted_M_norm.append(FrobeniusNorm(shifted_M[i]))
    percent_change.append((FrobeniusNorm(shifted_M[i])/A_norm)*100)
    
    corr, _ = pearsonr(FrobeniusNorm(shifted_M[i]), A_norm)
    corr_lst.append(float(corr))

print(len(percent_change))
print(percent_change)

print(len(shifted_M_norm))
print(shifted_M_norm)

fig, axes = plt.subplots(1, 3, figsize=(20,5))


plt.plot(s,percent_change,'ko-')

    

# %%
