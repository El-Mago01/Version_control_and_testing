import math
from curses.ascii import isdigit


def number_from_list(lst_of_digits):
    if len(lst_of_digits) == 0:
        raise ValueError("The list should contain at least 1 integer or more below 10")
    number = 0
    power=len(lst_of_digits)
    for digit in lst_of_digits:
        if not isinstance(digit, int):
            raise TypeError("The list should only contain integers below 10")
        if digit >=10:
            raise ValueError("The list should only contain integers below 10")
        number += digit*(math.pow(10,(power-1)))
        # print(number, power)
        power -= 1
    return number


