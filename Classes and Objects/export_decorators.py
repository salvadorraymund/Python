import functools

# @functools.wraps decorator which will preserve original information
# of the function being decorated with
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        rv = func(*args, **kwargs)
        return rv
    return wrapper_do_twice
