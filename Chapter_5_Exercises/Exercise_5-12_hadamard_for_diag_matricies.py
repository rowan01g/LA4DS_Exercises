#%%
import numpy as np 

D = np.diag(np.full(5,1))*np.array([1,2,3,4,5])
D2 = np.diag(np.full(5,1))*np.array([6,7,8,9,10])

print(f'{D}\n\n{D2}\n\n')

hadM = D*D2
mulM = D@D2

print(f'{hadM}\n\n{mulM}')

#Does the hadamard multiplication of D with D2 equal the matricx multiplication? 
np.all(np.isclose(hadM,mulM))

# %%
