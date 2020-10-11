def decorator_func(any_func):
    def wrapper_func():
        print('this is awesome')
        any_func()
    return wrapper_func    


@decorator_func
def func1():
    print('hello mdafaccka')

func1()

# ________________________________________________________________________________________________________________


from functools import wraps
def print_func_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'your function name is {function.__name__}')
        print(f'{function.__doc__}')
        return function(*args, **kwargs)
    return wrapper

@print_func_data
def add(a,b):
    """this takes two numbers and add them"""
    return a + b 

print(add(46,5))       


# ____________________________________


from functools import wraps
def only_int_allowed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args, **kwargs)
        else:
            return('this is an invalid shit!') 
    return wrapper

@only_int_allowed
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5,6,7,8,9))                 


# now with list comprehension

from functools import wraps
def only_int_allowed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg)==int for arg in args]):
          return function(*args, **kwargs)
        print('this is an invalid shit!')
    return wrapper

@only_int_allowed
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5,6,7,8,9))


#now with only data type


from functools import wraps
def only_data_type_allowed(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args, **kwargs)
            print('this is an invalid shit!')
        return wrapper
    return decorator
    
@only_data_type_allowed(str)
def string_joiner(*args):
    strings = ''
    for i in args:
        strings += i
    return strings

print(string_joiner('abhinav ', 'sahu'))