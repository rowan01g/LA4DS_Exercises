import matplotlib.pyplot as plt
import numpy as np
import math

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[1, 1])

#The array, elemnt list for mathematical manipluation and sum of squared elements
x = np.array([[1,2], [3, 4]])
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
print(f'The Euclidean norm of the array is: {math.sqrt(sum)}')



