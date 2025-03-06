#%%
import numpy as np 

def FrobeniusDistance(A,B): 
    M = A - B
    frob_dis = (np.sum(M**2))
    return frob_dis

A = np.random.randn(7,7)
B = np.random.randn(7,7)

s = 1
iteration = 0
AB_dis = FrobeniusDistance(A,B)
print(AB_dis)

while FrobeniusDistance(s*A, s*B) > 1:
    iteration += 1
    s *= 0.99
    if FrobeniusDistance(s*A, s*B) <= 1: 
        AB_dis_scaled = FrobeniusDistance(s*A, s*B) 
        break

print(f'The Frobenius/Euclidan Distance between random matricies A and B is {AB_dis_scaled} which took {iteration} interations to find the corerct scalars')


# %%
