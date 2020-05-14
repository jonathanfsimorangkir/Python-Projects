import numpy as np

# Title: Array Determinant Counter          detCounter(array)
# DEFENITION & SPECIFICATION:
# detCounter : two dimensional array of integer -> integer
#       - menghitung nilai determinan dari array berdimensi 2
#       - menghasilkan output bertipe bilangan bulat
#       - asumsi seluruh elemen pada array bertipe bilangan bulat

# REALIZATION
def detCounter(array):
    det_arr = round(np.linalg.det(array))
    return det_arr

# APPLICATION
# arr1 = [[1,2],[3,4]]
# arr2 = [[1,2,3],[4,5,6],[7,8,9]]
# detCounter(arr1)
# detCounter(arr2)
