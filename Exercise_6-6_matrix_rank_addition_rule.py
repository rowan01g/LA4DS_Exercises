#%% 
import numpy as np
import matplotlib.pyplot as plt

# r(A+B) =< r(A) + r(B)

a1 = np.array([[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               ])
a2 = np.array([[0, 2, 0],
               [0, 4, 0],
               [0, 6, 0],
               ])

print(np.linalg.matrix_rank(a1))
print(np.linalg.matrix_rank(a2))
# %%
