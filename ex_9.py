import time
from functools import wraps

def timer(func) : 
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling function {func.__name__} z parametrami args={args}, kwargs={kwargs}")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end  = time.perf_counter()
        elapsed = end - start
        print(f"[timer] Funkcja {func.__name__} zakończona w {elapsed:.6f} s, wynik = {result}")
        return result
    return wrapper
        
@timer        
def policz_sume(n):
    total = 0
    for i in range(n):
        total += i
    return total

suma = policz_sume(1_000_00)
print("Suma:", suma)


def timer_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print(f"this function: {func.__name__} is called with params args={args} and {kwargs}")
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"this function: {func.__name__} has eleapsed time {elapsed:.9f}")
        return result
    return wrapper

@timer_2
def count_for_me(n):
    gen = (n*n for n in range(n))
    yield gen
    

zmienna = count_for_me(1000)
print(f"zmienna {zmienna}")