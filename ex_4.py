from functools import wraps
import random
import time

def time_measurment(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end = time.time() 
        print(f"elapsed time is {end-start:.6f} s")
        return result
    return wrapper

@time_measurment
def randomize(ranges):
    rand = [random.randint(1,ranges) for _ in range(100) ]
    print(rand)
    return rand
    
randomize(1000)