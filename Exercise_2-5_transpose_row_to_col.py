import matplotlib.pyplot as plt 
import numpy as np 

v_row = np.array([[1,2,3],
                  [3,4,6]])
#reminder - v_row[i,j] - i is the row, j is the column which is why print returns 2
print(v_row[0,1])
print('/n')

v_row2 = np.array([1,2,3])
#initialise transpose vector
vt = np.zeros((3,1))
for i in range(v_row2.shape[0]):
    vt[i] = v_row2[i]

print(f'The transpose of {v_row2} is: \n {vt}')