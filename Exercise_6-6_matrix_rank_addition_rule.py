#%% 
import numpy as np
import matplotlib.pyplot as plt

# r(A+B) =< r(A) + r(B)

# a1 and a2 add to make a matrix with rank 0
a1 = np.array([[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               ])
a2 = np.array([[-1, 0, 0],
               [-2, 0, 0],
               [-3, 0, 0],
               ])

print(np.linalg.matrix_rank(a1))
print(np.linalg.matrix_rank(a2))

print(a1+a2)
print(np.linalg.matrix_rank(a1+a2))

#b1 and b2 add to make a matrix with rank 1 (The two non-zero columns of the summation are linearly dependant)
b1 = np.array([[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               ])
b2 = np.array([[0, 2, 0],
               [0, 4, 0],
               [0, 6, 0],
               ])

print(np.linalg.matrix_rank(b1))
print(np.linalg.matrix_rank(b2))

print(b1+b2)
print(np.linalg.matrix_rank(b1+b2))

c1 = np.array([[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               ])
c2 = np.array([[0, 5, 0],
               [0, 87, 0],
               [0, 0.3, 0],
               ])

print(np.linalg.matrix_rank(c1))
print(np.linalg.matrix_rank(c2))

print(c1+c2)
print(np.linalg.matrix_rank(c1+c2))




# %%
