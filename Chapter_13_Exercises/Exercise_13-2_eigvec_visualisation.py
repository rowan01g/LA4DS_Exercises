#%%
import numpy as np 
import matplotlib.pyplot as plt

A = np.array([ [-1,1],
               [-1,2] ])

eigval = np.linalg.eig(A)[0]
eigvec = np.linalg.eig(A)[1]

Av = A@eigvec

fig, axs = plt.subplots(figsize=(6,6))
axs.axhline(0, color='black', linewidth=0.5)  # x-axis
axs.axvline(0, color='black', linewidth=0.5)  # y-axis

#origin = np.zeros((2, 2))  # Origin for quiver plot

axs.plot([0,eigvec[0,0]],[0,eigvec[0,1]],'k',linewidth=2,label='v1')
axs.plot([0,Av[0,0]],[0,Av[0,1]],'k--',linewidth=2,label='Av1')

axs.plot([0,eigvec[1,0]],[0,eigvec[1,1]],'r',linewidth=2,label='v2')
axs.plot([0,Av[1,0]],[0,Av[1,1]],'r--',linewidth=2,label='Av2')

'''
# Plot original eigvec (blue)
axs.quiver(*origin, eigvec[0,0], eigvec[0,1], color=['green'], angles='xy', scale_units='xy', scale=1, label='v1')
axs.quiver(*origin, eigvec[1,0], eigvec[1,1], color=['blue'], angles='xy', scale_units='xy', scale=1, label='v2')

# Plot transformed eigvec (red)
axs.quiver(*origin, Av[0,0], Av[0,1], color=['red'], angles='xy', scale_units='xy', scale=1, label='Av1')
axs.quiver(*origin, Av[1,0], Av[1,1], color=['black'], angles='xy', scale_units='xy', scale=1, label='Av2')
'''
axs.set_xlim(-2, 2)
axs.set_ylim(-2, 2)
axs.set_xlabel("x-axis")
axs.set_ylabel("y-axis")
axs.set_title("Matrix A and A multiplied by EigenVector v")
axs.legend()
axs.grid()

plt.show()



# %%
