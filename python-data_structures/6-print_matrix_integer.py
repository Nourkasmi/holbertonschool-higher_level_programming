#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for i in range(len(num)):
            if i > 0:
                print(" ", end="")
            print("{:d}".format(num[i]), end="")
        print()
