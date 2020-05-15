import functions as f

# ***************************************************************************************
# Title: SPLNV (N Variables Linear Equation System) Calculator
# Author: Jonathan Fedrico Simorangkir
# Date: 2020
# Code Version: 1.0
# Availability: https://github.com/jonathanfsimorangkir/Python-Projects/tree/master/SPLNV
# ***************************************************************************************

# DESCRIPTIONS:
# 1. This program able to determine the value of N variables from N equations using Crammer Method
# 2. The given equation only contains integers
# 3. The program gives output only in the form of integers and fractions
# 4. The format for naming variables in the equation is as follows:
#   Equation-1 : (k1)X11 + (k2)X12 + (k3)X13 + ... + (kN)X1N = C1
#   Equation-2: (k1)X21 + (k2)X22 + (k3)X23 + ... + (kN)X2N = C2
#   .
#   .
#   Equation-N: (k1)XN1 + (k2)XN2 + (k3)XN3 + ... + (kN)XNN = CN

# GLOBAL THESAURUS:
# exit_program: boolean
# N, i, j, k, det_main_arr: integer
# arr_result: one dimensional array of integer [0..1]
# arr_eq, arr_eq_main, det_var_arr: two dimensional array of integer [0..N]
# arr_eq_x: three dimensional array of integer [0..N]

# ALGORITHM
exit_program = False
while not exit_program:
    # getting input of number of equation from users
    N = int(input("N: "))
    print()
    if N > 0:
        # creating array of equations
        arr_eq = [[0 for j in range(N + 1)] for i in range(N)]

        # getting input of equation element from users
        for i in range(N):
            print("Equation " + str(i + 1) + ": ")
            for j in range(N + 1):
                if j < N:
                    arr_eq[i][j] = int(input("Constant of X" + str(i + 1) + str(j + 1) + ": "))
                else:
                    arr_eq[i][j] = int(input("Constant of C" + str(i + 1) + ": "))
            print()

        # creating the main matrix
        arr_eq_main = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                arr_eq_main[i][j] = arr_eq[i][j]

        # creating variable matrix
        arr_eq_x = [[[0 for k in range(N)] for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if (k == i):
                        arr_eq_x[i][j][k] = arr_eq[j][N]
                    else:
                        arr_eq_x[i][j][k] = arr_eq[j][k]

        # finding the determinant of main matrix
        det_main_arr = int(round(f.detCounter(arr_eq_main)))

        # finding the determinant of each variable in variable matrix
        det_var_arr = [0 for i in range(N)]
        for i in range(N):
            determinan = f.detCounter(arr_eq_x[i])
            det_var_arr[i] = int(round(determinan))
        # finding and displaying the value of each variable
        print()
        print("Result:")
        if det_main_arr == 0:
            print("Error! Variables value not found.")
        else:
            for i in range(N):
                arr_result = f.fracSimp(abs(det_var_arr[i]), abs(det_main_arr))
                if (det_var_arr[i] < 0) and (det_main_arr < 0):
                    if arr_result[1] == 1:
                        print("Variable X" + str(i + 1) + " = " + str(arr_result[0]))
                    else:
                        print("Variable X" + str(i + 1) + " = " + str(arr_result[0]) + "/" + str(arr_result[1]))
                elif (det_var_arr[i] > 0) and (det_main_arr > 0):
                    if arr_result[1] == 1:
                        print("Variable X" + str(i + 1) + " = " + str(arr_result[0]))
                    else:
                        print("Variable X" + str(i + 1) + " = " + str(arr_result[0]) + "/" + str(arr_result[1]))
                else:
                    if arr_result[1] == 1:
                        print("Variable X" + str(i + 1) + " = -" + str(arr_result[0]))
                    else:
                        print("Variable X" + str(i + 1) + " = -" + str(arr_result[0]) + "/" + str(arr_result[1]))
    else:
        print("Error! Can't assign value of N <= 0")
    print()
    closing_question = input("Try again? (Y/N): ")
    if (closing_question == 'Y') or (closing_question == 'y'):
        print()
    else:
        print()
        print("Thank you for using this program!")
        exit_program = True
