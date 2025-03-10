import matplotlib.pyplot as plt
import numpy as np
import math


def euclidean_norm(x):
    elements_list = []
    sum = 0

    #Converts numpy scalars to python scalar
    x = x.tolist()

    #iterates through numpy array (now converted to list) for each element and appends to elemets_list
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j]) 
            elements_list.append(x[i][j])
    print(f'The elements of the array have been converted to Python scalars and inserted into the list:{elements_list}')

    for e in elements_list: 
        sum += e**2
    print(f'The sum of all the elements within the array is: {sum}')
    print(f'The Euclidean norm of the array is: {math.sqrt(sum)} calculated by manual iteration and operations on the elements')

    print(f'The function used to calculate the Euclidean norm is np.linalg.norm and for the array x, it has retuned: {np.linalg.norm(x)}')

#The array, elemnt list for mathematical manipluation and sum of squared elements
array1 = np.array([[1,2], [3, 4]])
euclidean_norm(array1)
