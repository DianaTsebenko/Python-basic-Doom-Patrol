from datetime import datetime
import os


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        if os.path.exists('log.txt'):
            pass
        elif not os.path.exists('log.txt'):
            file = open('log.txt', 'w')
            file.close()
        log = f'{self.func.__name__} with was executed at {datetime.now()}\n'
        print(log)
        with open('log.txt', 'a') as file:
            file.write(log)


@Logger
def my_func():
    """
    This is my func
    """
    print(f"{my_func().__name__} is running")


my_func()
