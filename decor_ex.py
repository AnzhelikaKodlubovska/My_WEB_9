import datetime
import time

def sum_numbers(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        # time.sleep(2)
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()       
        delta = start_time - end_time 
        return delta 
    return wrapper


@sum_numbers
def add(a, b):
    return a + b


print(add(1011111111, 12222222))