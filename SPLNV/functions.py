import numpy as np


# MAIN FUNCTIONS

# ******************************************************************************************************

# Title: Array Determinant Counter          detCounter(array)
# DEFENITION & SPECIFICATION:
# detCounter : two dimensional array of integer -> integer
#       - menghitung nilai determinan dari array berdimensi 2
#       - menghasilkan output bertipe bilangan bulat
#       - asumsi seluruh elemen pada array bertipe bilangan bulat

# REALIZATION
def detCounter(array):
    det_arr = np.linalg.det(array)
    return det_arr

# APPLICATION
# arr1 = [[1,2,3],[4,5,6],[7,8,9]]
# detCounter(arr1)

# ******************************************************************************************************

# TITLE: Fractional Simplifier          fracSimp(numerator,denominator)
# DEFENITION & SPESIFICATION:
# fracSimp(numerator,denominator) : integer,integer -> array of integer
#       - menerima input berupa dua bilangan integer positif
#       - mengubah pembilang dan penyebut menjadi bentuk yang paling sederhana
#       - memberikan keluaran berupa array of integer yang berisikan 2 elemen:
#           - Elemen 1 (index = 0) merupakan pembilang yang telah disederhanakan
#           - Elemen 2 (index = 1) merupakan penyebut yang telah disederhanakan

# REALIZATION
def fracSimp(numerator, denominator):
    # find the GCD between numerator and denominator
    gcd = hitung_FPB(numerator, denominator)
    simp_num = int(numerator / gcd)
    simp_den = int(denominator / gcd)
    # creating the output array
    arr_out = [simp_num, simp_den]
    return arr_out

# APPLICATION
# fracSimp(125, 25)


# ADDITIONAL FUNCTIONS

# ******************************************************************************************************
# Title: Greatest Common Divisor (GCD) counter - FPB        hitung_FPB(x, y)
# Author: pythonindo
# Date: -
# Code Version: -
# Availability: https://www.pythonindo.com/menentukan-faktor-persekutuan-terbesar-fpb-menggunakan-python/

# DEFENITION & SPESIFICATION:
# hitung_FPB : integer, integer -> integer
#       - Able to determine the GCD of 2 integers
#       - Request 2 inputs as integers
#       - Produces an integer output

# REALIZATION
def hitung_FPB(x, y):
    # choose the smallest number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            fpb = i
    return fpb

# APPLICATION
# print(hitung_FPB(100, 25))
