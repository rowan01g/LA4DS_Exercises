#%%
import numpy as np 

#The Frobenius norm can be calculated as the Square root of the trace of the matrix times its transpose

def random_matrix():
    M = np.random.randint(low=0, high=11, size = 100).reshape(10,10)
    return M 

def calc_frob_norm(M):
    F = (np.trace(M@M.T))**0.5
    return F

frob_norm_lst = []
for i in range(40):
    n = calc_frob_norm(random_matrix())*np.random.randint(low=-50, high=51)
    frob_norm_lst.append(n)

print(frob_norm_lst)
print(len(frob_norm_lst))
# %%
