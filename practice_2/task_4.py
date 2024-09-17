# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""
import typing as tp


def find_sum_of_digits() -> tp.Optional[int]:
    number: str = input()

    try:
        int(number)
    except:
        print("Это не число, что вы сюда ввели?")
        return None

    if (len(number) != 4 and len(number) != 5) or (len(number) == 5 and number[0] != '-') or (len(number) == 4 and number[0] == '-'):
        print("Число не четырёхзначное")
        return None

    sum_digits = 0
    for digit in number:
        if digit != '-':
            sum_digits += int(digit)

    return sum_digits


print(find_sum_of_digits())
