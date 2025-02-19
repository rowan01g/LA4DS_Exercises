#%%
import numpy as np 
import matplotlib.pyplot as plt

v = np.random.randn(2)
w = np.random.randn(2)

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
print(f'The value of the scalar beta is {beta} (The point at which the head of the vecotr, b, is as close as possible to vecotr a)')

#calculate vector parallel to reference vector. parallel vector = reference vector * beta
para = a*beta
#calculate vector perpendicular to reference vector. perpendicular vector = target vector - parallel vector
perp = b - para

a1 = plt.arrow(0, 0, a[0], a[1], color='k',length_includes_head=True, head_width = .02*np.diff(plt.xlim())[0], width = .01*np.diff(plt.xlim())[0])
a2 = plt.arrow(0, 0, b[0], b[1] ,color='k',length_includes_head=True, head_width = .02*np.diff(plt.xlim())[0], width = .01*np.diff(plt.xlim())[0])
#vector parallel to reference vector, scaled by beta
a3 = plt.arrow(0, 0, para[0], para[1],color='r',length_includes_head=True, head_width = .02*np.diff(plt.xlim())[0], width = .01*np.diff(plt.xlim())[0])
#vector perpendicular to reference vector 
a4 = plt.arrow(0, 0, perp[0], perp[1], color='b',length_includes_head=True, head_width = .02*np.diff(plt.xlim())[0], width = .01*np.diff(plt.xlim())[0])

#dashed projection lines
plt.plot([b[0],para[0]],[b[1],para[1]],linewidth=.5,color='0.5', linestyle = '--')
plt.plot([perp[0], b[0]],[perp[1], b[1]], linewidth=.5,color='0.5', linestyle = '--')

plt.grid(linestyle='--', linewidth= 0.5)
plt.axis('square')
plt.axis('equal')

#if the result is correct, the dot product between two orthoganal vectors must be 0 in this case, the reference vector, a, and the perpendicular vector
tolerance = 1e-10
if np.dot(a, perp) < tolerance: 
    print(f'The dot product between the reference vector and the perpendicular vector is {np.dot(a, perp)} (very close to 0, accounting for error) and the caluclation is correct')
else: 
    print(f'The dot product between the reference vector and the supposed perpendicular vector is {np.dot(a, perp)} and the caluclation is incorrect, suggesting an error in the mathemathical code')

plt.show()
# %%
