import datetime
import json

import psutil
import os

def MEMORYTime(func):
    '''
    Принимается на вход Функиця которую надо замерить
    \n на критерии:
    \n - 1 . Job Time
    \n - 2 . Usage memory


    Пример Вывода (print) функции :

    \n - Занятая памать (MB): int | float
    \n - Занятая памать (KB): int | float
    \n - Время работы: day . hour . minutes . sekond . miliSekond

    :return:  Print
    '''
    def wrapper():
        memory: dict[str:int] = {'KB': 1024, 'MB': (1024 * 1024)}
        def memory_usage(type):
            process = psutil.Process(os.getpid())
            return process.memory_info().rss / memory[type]
        # фиксируем и выводим время старта работы кода
        start = datetime.datetime.now()
        # print('Время старта: ' + str(start))
        memory_before_MB = memory_usage('MB')
        memory_before_KB = memory_usage("KB")
        func()
        memory_after_KB = memory_usage("KB")
        memory_after_MB = memory_usage("MB")
        #фиксируем и выводим время окончания работы кода
        finish = datetime.datetime.now()
        # print('Время окончания: ' + str(finish))
        print(f"Занятая памать (MB): {round(memory_after_MB - memory_before_MB, 2)}")
        print(f"Занятая памать (KB): {round(memory_after_KB - memory_before_KB, 2)}")
        # вычитаем время старта из времени окончания
        print('Время работы: ' + str(finish - start))

    return wrapper()
