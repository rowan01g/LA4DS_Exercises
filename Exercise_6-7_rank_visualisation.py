#%%
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt
"""
def RandMatrix(): 
    M = int(input('Please input a value to M to make a MxM matrix: '))
    r = int(input('Please input a value for the rank of the matrix, note - if your value of r is greater than M, your matrix rank will be full-rank and equal to M: '))

    #if r is less than M, rank of the matrix equals r
    # if r is greater than M, rank of the matrix equals M - (becomes a full rank matrix)

    m1 = np.random.randn(M,r)
    m2 = np.random.randn(r,M)
    m1m2 = m1@m2

    if r < M:
        print(f'Your {M} x {M} matrix has a rank of {np.linalg.matrix_rank(m1m2)}')
    else:
        print(f'Your {M} x {M} matrix is full rank and has a rank of {np.linalg.matrix_rank(m1m2)} - though your selected value of r was {r}')

    print(m1m2)
    return np.linalg.matrix_rank(m1m2)

RandMatrix()"
"""
def RandMatrix(M,r): 
    
    m1 = np.random.randn(M,r)
    m2 = np.random.randn(r,M)
    m1m2 = m1@m2

    return m1m2

r = 2
A_list = []
B_list = []
for _ in range(14):
    X = RandMatrix(20, r)
    A_list.append(X)
    B_list.append(X)
    r += 1

print(f'The length of A_list is: {len(A_list)}')
print('The ranks of the matricies in A_list is: ')
for i in range(len(A_list)):
    print(np.linalg.matrix_rank(A_list[i]), end=" ")

AB_sum = np.zeros(196).reshape(len(A_list),len(A_list))
print(f'\n{AB_sum}')

for i in range(len(A_list)):
    for j in range(len(B_list)):
        AB_sum[i,j] = np.linalg.matrix_rank(A_list[i]+B_list[j])


print(f'\n{AB_sum}')

fig, axes = plt.subplots(1, 3, figsize=(20,5))

vmin=2
vmax=15

AB_sum_hm = sns.heatmap(data=AB_sum, ax=axes[0], cmap='mako', annot=True, vmin=vmin, vmax=vmax)







# %%
