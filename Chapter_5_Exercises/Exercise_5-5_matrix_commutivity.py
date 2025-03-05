#%%
import numpy as np 

xlim=(0,10)

A = np.random.randint(low=xlim[0], high=xlim[1], size = 12).reshape(3,4)
B = np.random.randint(low=xlim[0], high=xlim[1], size = 12).reshape(3,4)
S = np.random.randint(low=xlim[0], high=xlim[1])

#S(A+B)
x = S*(A+B)

#SA + SB
y = S*A + S*B

#AS + BS 
z = A*S + B*S

if np.array_equal(x, y) and np.array_equal(y, z):
    print('x = y = z and the equations are commutitive and distributitive')
else: 
    print('There is an error in the code')

# %%
