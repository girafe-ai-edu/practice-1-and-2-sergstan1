# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""

import typing as tp


def find_bmi() -> tp.Optional[float]:
    height = int(input())
    weight = int(input())
    if height == 0:
        print('Can not compute BMI')
        return None
    return weight / height**2


print(find_bmi())
