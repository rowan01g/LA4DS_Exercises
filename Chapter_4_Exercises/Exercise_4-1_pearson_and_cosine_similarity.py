#%%
import numpy as np 
from scipy.stats import pearsonr

def pearson_calc():
    xlim = [0, 100]
    v1 = np.random.uniform(low=xlim[0], high=xlim[1], size=(100,))
    v2 = np.random.uniform(low=xlim[0], high=xlim[1], size=(100,))
    print(v1)
    print(f'v1 shape is {v1.shape[0]}')

    # Find the mean of the varibales within each vector
    v1_sum = 0 
    for i in range(len(v1)):
        v1_sum += v1[i]
    print(f'The sum of the variables within the single row vector, v1 is {v1_sum}')

    v2_sum = 0 
    for i in range(len(v2)):
        v2_sum += v2[i]
    print(f'The sum of the variables within the single row vector, v2 is {v2_sum}')

    v1_mean = v1_sum/len(v1)
    v2_mean = v2_sum/len(v2)
    print(f'The mean of the variables within the single row vector, v1 is {v1_mean}')
    print(f'The mean of the variables within the single row vector, v2 is {v2_mean}')

    # Mean center each varibale within vectors v1 and v2 
    # initialise mean centered arrays 
    v1_cntrd = np.zeros([100,])
    v2_cntrd = np.zeros([100,])

    for i in range(v1.shape[0]): 
        v1_cntrd[i] = v1[i] - v1_mean

    for i in range(v2.shape[0]): 
        v2_cntrd[i] = v2[i] - v2_mean

    # Take the dot product of the mean centered vectors
    dot_v1v2 = np.dot(v1_cntrd,v2_cntrd)
    print(f'The dot product betwen the mean-centered variables of vectros v1 and v2 are: {dot_v1v2}')

    #Denominator of pearson calculation 
    # Take the square of the of the mean centerd value 
    v1_cntrd_sqrd = np.zeros([100,])
    for i in range(v1_cntrd.shape[0]): 
        v1_cntrd_sqrd[i] = v1_cntrd[i]**2

    v2_cntrd_sqrd = np.zeros([100,])
    for i in range(v2_cntrd.shape[0]): 
        v2_cntrd_sqrd[i] = v2_cntrd[i]**2

    # sum all the values within the centerd and squared vectors
    v1_cntrd_sqrd_sum = 0
    for i in range(v1_cntrd_sqrd.shape[0]):
        v1_cntrd_sqrd_sum += v1_cntrd_sqrd[i]

        v2_cntrd_sqrd_sum = 0
    for i in range(v2_cntrd_sqrd.shape[0]):
        v2_cntrd_sqrd_sum += v2_cntrd_sqrd[i]

    denom = (v1_cntrd_sqrd_sum**0.5)*(v2_cntrd_sqrd_sum**0.5)
    r_value = dot_v1v2/denom
    print(f'The pearson correlation coefficicient, r, calculated manually is: {r_value}')

    #Verification of correct calculation with pearsonr calcualtion from library 
    # Is indeed correct!!
    lib_r_value = pearsonr(v1,v2) 
    print(lib_r_value)

def cosine_sim():
    #make dot product global then divid by product of mean centered norms



pearson_calc()

 
# %%
