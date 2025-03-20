#%%

import numpy as np 
import matplotlib.pyplot as plt

#not very elegenat but hey ho 
M_size = []
for m in range(3,31):
    M_size.append(m*m)

M_list = []
det_lists = {}

for exp_num in range(1, 101):

    det_list = []

    for m in range(3, 31):
        M = np.random.randn(m*m).reshape(m,m)
        # Set the far right column of the matric to be multiple of 2 of the second last column, creating a reduced-rank matrix
        M[:,-1] = M[:,-2]*2
        det = np.linalg.det(M)
        M_list.append(M)
        det_list.append(det)
    
    det_lists[f"det_list_{exp_num}"] = det_list

det_matrix = np.array(list(det_lists.values())) # turns dictionary into a matrix
det_summed = np.sum(det_matrix, axis=0)  # Summed across all 100 lists (column wise)
print(det_summed)

avg_det_list = []
for i in range(len(det_summed)): 
    avg_det = det_summed[i]/100
    avg_det_list.append(avg_det)

# Compute the log of the absolute determinant to avoid log(negative numbers)
log_det = np.log(np.abs(avg_det_list))
print(log_det)
print(len(M_size))

plt.figure(figsize=(8, 5))
plt.plot(M_size, log_det, marker='o', linestyle='-', color='b', label="Determinant")

plt.xlabel("Matrix Size (m * m)")
plt.ylabel("Log Determinant")
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
