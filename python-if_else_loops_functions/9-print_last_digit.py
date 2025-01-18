#!/usr/bin/python3
def print_last_digit(digit):
    last = abs(digit) % 10
    print(last, end="")
    return last
