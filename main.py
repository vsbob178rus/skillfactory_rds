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
 def score_game(game_number):
    '''Запускаем игру 1000 раз'''
    count_ls=[]
    np.random.seed(1)
    random_array=np.random.randint(1, 101, size=(1000))
    for number n random array:
        count_ls.append(game_number(number)
    score=int(np.mean(count_ls))
    print(f"ваш алгоритм угадывает число за {score} попыток")
    return(score)
score_game(game_number)