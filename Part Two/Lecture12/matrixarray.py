import numpy as np


def set_array(L, rows, cols):
    if len(L) != rows*cols:
        print("Length doesn't match")
    arr = np.empty((rows, cols))
    index= 0
    for i in range(rows):
        for j in range(cols):
            arr[i,j] = L[index]
            index+=1
    return arr


L = [1, 2, 3, 4, 5, 6]
rows, cols = 2, 3

returned_arr = set_array(L, rows, cols)
print("Array:")
print(returned_arr)

        

