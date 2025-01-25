#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    y = 0
    for numeral in roman_string:
        value = x.get(numeral, 0)
        if value > y:
            total += value - 2 * y
        else:
            total += value
        y = value
    return total
