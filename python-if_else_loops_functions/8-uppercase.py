#!/usr/bin/python3

def uppercase(str):
    result = ""
    for num in str:
        if 97 <= ord(num) <= 122:
            result += chr(ord(num) - 32)
        else:
            result += num
    print(result)
