import matplotlib.pyplot as plt 
import numpy as np 

# any nonunit vector has an unit vector associated unit vector. A unit vector has a geometric length (magnitude) of 1 - if associated with a nonunit vecotr, it will be in the same direction

def create_unit_vector(v):
    v_norm = np.linalg.norm(v)
    print(f'The Euclidean norm of your array is: {v_norm}')
#scalar multiplcation of v with the reciprocal norm to get the unit vector
    v_hat = v/v_norm
    print(f'The magnitude of the vector is now: {v_hat}')

array1 = np.array([3,4])
create_unit_vector(array1)


    