from functools import wraps
from time import time


def timethis(f):
    def timethis_f(*args, **kwargs):
        start = time()
        r = f(*args, **kwargs)
        end = time()
        print(f"{f.__module__}.{f.__name__}: {end-start}")
        return r

    return timethis_f
