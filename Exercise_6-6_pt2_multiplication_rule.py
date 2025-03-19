#%% 
import numpy as np
import matplotlib.pyplot as plt

# r(A+B) =< r(A) + r(B)

# a1 and a2 multiply to make a matrix with rank 
a1 = np.array([[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               ])
a2 = np.array([[-1, 0, 0],
               [-2, 0, 0],
               [-3, 0, 0],
               ])

print(a1@a2)
print(f'The rank of the a1@a2 matrix is : {np.linalg.matrix_rank(a1+a2)}')

#b1 and b2 multiply to make a matrix with rank 
b1 = np.array([[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               ])
b2 = np.array([[0, 2, 0],
               [0, 4, 0],
               [0, 6, 0],
               ])

print(b1@b2)
print(f'The rank of the b1@b2 matrix is : {np.linalg.matrix_rank(b1+b2)}')

#c1 and c2 multiply to make a matrix with rank 
c1 = np.array([[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               ])
c2 = np.array([[0, 5, 0],
               [0, 87, 0],
               [0, 0.3, 0],
               ])

print(c1@c2)
print(f'The rank of the c1@c2 matrix is: {np.linalg.matrix_rank(c1+c2)}')

# %%
