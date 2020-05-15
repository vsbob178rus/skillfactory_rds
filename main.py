import numpy as np
''' Задача для поиска загаданного числа'''
def game_number(number):
    digit_list=[i for i in range(1, 101)]
    low=digit_list[0]
    high=digit_list[-1]
    i=0