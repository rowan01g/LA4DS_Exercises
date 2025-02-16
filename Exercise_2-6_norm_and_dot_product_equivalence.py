#The SQUARED norm (euclidean formula is square-rooted so square it to cancel it out) of a vector is equivalent to the dot product that vector with itself - and I'll prove it 

import numpy as np
import math

v = np.array([1,2,3])

#Calculating the Euclidean norm (the magnitiude)
v_sum = 0
for i in v:
    v_sum += i**2
    v_norm = math.sqrt(v_sum)

v_norm_sqrd = v_norm**2
print(f'The square of the norm is: {v_norm_sqrd}')

#Calculating the dot product

w = v*v
print(w)
dot_w = 0
for i in w: 
    dot_w += i
print(f' The dot product of vector with itself is : {dot_w}')
