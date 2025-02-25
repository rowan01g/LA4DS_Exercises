#%%

import numpy as np 

xlim = [0, 100]
v1 = np.random.uniform(low=xlim[0], high=xlim[1], size=(1,100))
v2 = np.random.uniform(low=xlim[0], high=xlim[1], size=(1,100))
print(v1)
print(v1.shape[1])

# Find the mean of the varibales within each vector
v1_sum = 0 
for i in range(v1.shape[1]):
    v1_sum += v1[0,i]
print(f'The sum of the variables within the single row vector, v1 is {v1_sum}')

v2_sum = 0 
for i in range(v2.shape[1]):
    v2_sum += v2[0,i]
print(f'The sum of the variables within the single row vector, v1 is {v2_sum}')

v1_mean = v1_sum/len(v1[0])
v2_mean = v2_sum/len(v2[0])
print(f'The mean of the variables within the single row vector, v1 is {v1_mean}')
print(f'The mean of the variables within the single row vector, v2 is {v2_mean}')

# Mean center each varibale within vectors v1 and v2 
# initialise mean centered arrays 
v1_cntrd = np.zeros([1,100])
v2_cntrd = np.zeros([1,100])

for i in range(v1.shape[1]): 
    v1_cntrd[0:i] = v1[0:i] - v1_mean

for i in range(v2.shape[1]): 
    v2_cntrd[0:i] = v2[0:i] - v2_mean

print(v1_cntrd)

# Take the dot product of the mean centered vectors




 
# %%
