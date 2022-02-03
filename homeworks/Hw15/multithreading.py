import time
import threading


def get_threads_count():
    num = threading.active_count()
    print(f'Running threads: {num}')


def calculation():
    start = time.time()
    a = [x ** 3 for x in range(1500000)]
    time_result = time.time() - start
    print(round(time_result, 3), 'seconds')


get_threads_count()
calculation()

thread_1 = threading.Thread(target=get_threads_count)
thread_2 = threading.Thread(target=calculation)

start1 = time.time()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print(f'Two threads total time: {time.time() - start1}')
