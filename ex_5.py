import time
from functools import wraps

def time_count(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        print("args:", args)
        print("kwargs:", kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"funkcja {func.__name__} wykonała się w czasie {elapsed:.12f} sec.")
        return func
    return wrapper
        
@time_count
def policz(number):
    s=0
    for i in range(100000):
        s+=i
        print(s)
policz(10)
