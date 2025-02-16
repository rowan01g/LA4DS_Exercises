import numpy as np

# commutative definiton: group of quantitites connected by operators give the same results regarldess of order of quanttiies 
# e.g a*b = b*a

v = np.array([1,2,3])
w = np.array([3,4,5])

v_mul = v*w
v_dot = 0
for i in v_mul: 
    v_dot += i

w_mul = w*v 
w_dot = 0
for i in w_mul: 
    w_dot += i

if v_dot == w_dot: 
    print(f'The dot products between arrays: {v} and {w} are communicative and : {v_dot} = {w_dot}')
else: 
    print('The dot products are not communicative')