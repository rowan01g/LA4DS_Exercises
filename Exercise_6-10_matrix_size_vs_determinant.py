#%%

import numpy as np 
import matplotlib.pyplot as plt

M_size = []
M_list = []
det_list = []
for m in range(3, 30):
    M = np.random.randn(m*m).reshape(m,m)
    # Set the far right column of the matric to be multiple of 2 of the second last column, creating a reduced-rank matrix
    M[:,-1] = M[:,-2]*2
    det = np.linalg.det(M)
    M_size.append(m*m)
    M_list.append(M)
    det_list.append(det)

# Compute the log of the absolute determinant to avoid log(negative numbers)
log_det = np.log(np.abs(det_list))

plt.figure(figsize=(8, 5))
plt.plot(M_size, log_det, marker='o', linestyle='-', color='b', label="Determinant")

plt.xlabel("Matrix Size (m * m)")
plt.ylabel("Determinant")
plt.title("Matrix Size vs Determinant")
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Add horizontal line at y=0
plt.legend()
plt.grid(True)

print(len(M_list))
print(np.shape(M_list[0]))
print(np.shape(M_list[1]))
print(np.linalg.matrix_rank(M_list[1]))
print(M_list[1])
# %%
