#%%
import numpy as np 
import matplotlib.pyplot as plt

v = np.array([2,4])
w = np.array([2,1])

#calulate the euclidean norm of the vetors to obtain the magnitude
v_norm = np.linalg.norm(v)
w_norm = np.linalg.norm(w)

#Calculates which of the vectors has a greater magnitude - which will allow is to calcuate Beta
if v_norm > w_norm: 
    print(f'v_norm: {v_norm} is bigger than w_norm: {w_norm}')
    a = v 
    b = w
else: 
    a = w
    b = v

beta = np.dot(a,b)/np.dot(a,a)
print(f'The value of the scalar beta is {beta} (The point at which the head of the vecotr, b, is as close as possible to vecotr a )')

a1 = plt.arrow(0, 0, a[0], a[1], head_width=.15,width=.05,color='k',length_includes_head=True)
a2 = plt.arrow(0, 0, b[0], b[1], head_width=.15,width=.05,color='k',length_includes_head=True)

#projection line - note, this does not works as plt.arrow takes x,y, dx,dy I have inputed absolute coordnates whereas the finction takes change in coordinates - therefore, plt.plt is more effective
#a3 = plt.arrow(b[0], b[1], beta*b[0], beta*a[1], head_width=.15,width=.05,color='k',length_includes_head=True)

#plt plot takes coordinates as [x,x], [y,y] 
plt.plot([b[0],beta*b[0]],[b[1],beta*a[1]],linewidth=.5,color='0.5', linestyle = '--')



plt.grid(linestyle='--', linewidth= 0.5)
plt.axis('square')
plt.axis([-2,6,-2,6])


plt.show()

# %%
