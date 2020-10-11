from functools import wraps
import time


def calculate_time(function):
    @wraps(function)
    def wrapper_func(*args, **kwargs):
        print(f'executing....{function.__name__}')
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()    
        time_taken = t2 - t1
        print(f'this function took {time_taken} seconds to run this code')
        print('this is our fckin function')
        print('this our freaky function')
        print('this shit is our function')
        return returned_value
    return wrapper_func
    
@calculate_time
def square_find(n):
        return[i**2 for i in range(1,n+1)],


print(square_find(2000))



