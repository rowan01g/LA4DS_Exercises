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
AB_prod = np.zeros(196).reshape(len(A_list),len(A_list))
print(f'\n{AB_sum}')

for i in range(len(A_list)):
    for j in range(len(B_list)):
        AB_sum[i,j] = np.linalg.matrix_rank(A_list[i]+B_list[j])
        AB_prod[i,j] = np.linalg.matrix_rank(A_list[i]@B_list[j])


print(f'\n{AB_sum}')

fig, axes = plt.subplots(1, 2, figsize=(25,10))

vmin=2
vmax=15

AB_sum_hm = sns.heatmap(data=AB_sum, ax=axes[0], cmap='mako', annot=True, vmin=vmin, vmax=vmax)
axes[0].invert_yaxis()

AB_prod_hm = sns.heatmap(data=AB_prod, ax=axes[1], cmap='mako', annot=True, vmin=vmin, vmax=vmax)
axes[1].invert_yaxis()


tick_labels = list(range(2, 16))  # Labels from 2 to 15
axes[0].set_xticks(np.arange(len(tick_labels)) + 0.5)  # Set tick positions
axes[0].set_yticks(np.arange(len(tick_labels)) +0.5 ) # + 0.5 sets ticks on the squares of the grid
axes[0].set_xticklabels(tick_labels)  # Set tick labels
axes[0].set_yticklabels(tick_labels)
axes[1].set_xticks(np.arange(len(tick_labels)) + 0.5)  # Set tick positions
axes[1].set_yticks(np.arange(len(tick_labels)) +0.5 ) # + 0.5 sets ticks on the squares of the grid
axes[1].set_xticklabels(tick_labels)  # Set tick labels
axes[1].set_yticklabels(tick_labels)

# Set axis labels
axes[0].set_xlabel("Rank of Matrix B")
axes[0].set_ylabel("Rank of Matrix A")
axes[1].set_xlabel("Rank of Matrix B")
axes[1].set_ylabel("Rank of Matrix A")

#set axis titles 
axes[0].set_title("Rank of A+B", fontsize=14)
axes[1].set_title("Rank of A@B", fontsize=14)







# %%
