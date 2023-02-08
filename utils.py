import sys


def try_block(function, *args, **kwargs):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(function.__name__, sys.exc_info())
    return wrapper
