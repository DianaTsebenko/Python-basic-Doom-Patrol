import math
from multiprocessing import Process
import os


def quadratic_calculator(a, b, c):
    dis = (b ** 2) - (4 * a * c)

    if dis > 0:
        x1 = (-b - math.sqrt(dis)) / (2 * a)
        x2 = (-b + math.sqrt(dis)) / (2 * a)
        print(f'Result: {round(x1)} and {round(x2)}')
    elif dis == 0:
        x1 = x2 = -b / (2 * a)
        print(f'Result: {round(x1)} and {round(x2)}')
    elif dis < 0:
        print('The quadratic equation has no real roots')


process_1 = Process(target=quadratic_calculator(6, 11, -35))
process_2 = Process(target=quadratic_calculator(5, -2, -9))

process_1.start()
process_2.start()

process_1.join()
process_2.join()
