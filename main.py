import numpy as np
''' Задача для поиска загаданного числа'''
def game_number(number):
    digit_list=[i for i in range(1, 101)]
    low=digit_list[0]
    high=digit_list[-1]
    i=0
    while low<=high:
        i+=1
        middle=(low+high)//2
        if middle>number:
            high=middle-1
        elif middle<number:
            low=middle+1
        else:
            break
    return(i)