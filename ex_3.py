
from functools import wraps

def hello(func):
    def wrapper():
        print ("Hello!")
        return func()
    return wrapper
    
@hello
def original_fun():
    name="pies"
    print(f"to jest {name}")
    
'''example for generators'''
def square(numbers):
    for i in numbers:
        yield i*i

'''generator in square function with yield'''
numbers = square([1,2,3,4,5])   
print('square numbers are')
for num in numbers:
    print(num)
    
'''list comprehension'''
nums = [x*x for x in [1,2,3,4,5,6,7,8,9,10]]
print('list comprahension', nums)

'''generator made from list comprehension - [] changed into parentheses'''
nums2 = (x*x for x in [1,2,3,4,5,6,7,8,9,10])
for num in nums2:
    print('nums2 with genrator made ',next(nums2))

'''second example'''
def time_count(func):
    def wrapper(*args, **kwargs):
        
        return None
    return None

def original_fun_2():
    art = "czlowiek"
    

'''wrapper regular'''

def hello_to_name(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        name = func(*args,**kwargs)
        print(f"hello to {name}")
        
    return wrapper
@hello_to_name
def saying_hello(name):
    print(name)
    return name


original_fun()
original_fun_2()
saying_hello("Maciej")