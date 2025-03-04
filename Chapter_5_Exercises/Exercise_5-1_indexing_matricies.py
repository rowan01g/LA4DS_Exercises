#%%
import numpy as np

M = np.arange(12).reshape(3,4)
print(f'the matrix is: \n{M}')

while True:
    row = int(input('Please choose a row number between 1 and 3: ')) 
    if 1 <= row <= 3:
        break  # Exit the loop if the row is valid
    else: 
        print('Please select a valid row number between 1 and 3')

while True:
    column = int(input('Now, select a column number between 1 and 4:')) 
    if 1 <= column <= 4:
        break  # Exit the loop if the row is valid
    else: 
        print('Please select a valid column number between 1 and 4')

row_index = row -1
column_index = column -1 

print(f'Your selected matrix element is at row position {row} and column position {column} is {M[row_index, column_index]}')


 
# %%
