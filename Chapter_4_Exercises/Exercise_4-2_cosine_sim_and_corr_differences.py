#%%
import numpy as np 
from scipy.stats import pearsonr
from numpy import dot 
from numpy.linalg import norm

v1 = np.arange(0,4)
#[:, None] turns the single row array into a column array
v2 = np.arange(-50, 51)[:, None]*np.ones((1,4), dtype=int)

#initialise zeros vector to store offset values 
v3 = np.zeros((101,4),dtype=int)
for i in range(len(v2)):
    v3[i] = (v2[i] + v1)

print(f'The first 5 Rows of vector v3 are:\n{v3[0:6]}')

#calculate the mean offset of the vectors in v3 

v3_mean = np.mean(v3, axis = 1)
print(v3_mean[0:6])

#compute the pearson r of v1 with v3 vector elements for n vectors in v3 
r = []
for i in range(len(v3)):
    corr, _ = pearsonr(v3[i],v1) 
    r.append(float(corr))
print(r)    

#compute the cosine similarity of v1 with v3 vector elements for n vectors in v3 
c = []
for i in range(len(v3)):
    cos_sim = dot(v1,v3[i])/(norm(v1)*norm(v3[i]))
    c.append(float(cos_sim))
print(c)

    




# %%
