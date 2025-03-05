#%%
import numpy as np 

A = np.ones(16).reshape(4,4)
D = np.diag(np.full(4,1))*np.array([1,4,9,16])
D2 = D**0.5

print(f'{A}\n\n{D}\n\n{D2}')

#premultiplied diagonal matrix with ones matrix 
DA = D@A
print(f'\n\n{DA}')
#postmultiplied diagoinal matrix with ones matrix
AD = A@D 
print(f'\n\n{AD}')

#pre and postmultiplied sqrt diagonal matrix with ones matrix 
D2AD2 = D2@A@D2
print(f'\n\n{D2AD2}')

# %%
