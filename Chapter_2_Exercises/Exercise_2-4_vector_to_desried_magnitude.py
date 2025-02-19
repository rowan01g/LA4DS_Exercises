import matplotlib.pyplot as plt 
import numpy as np 

#fisrt calculate the unit vector and then scalar multiply this by desired magnitude from user input 

def create_unit_vector(v):
    m = input('Please input a magnitude to scale your vector: ')
    v_norm = np.linalg.norm(v)
    print(f'The Euclidean norm of your array is: {v_norm}')
#scalar multiplcation of v with the reciprocal norm to get the unit vector
    v_hat = v/v_norm*int(m)
    print(f'Scaled to your value of {3}, the magnitude of the vector is now: {v_hat}')

array1 = np.array([3,4])
create_unit_vector(array1)


    