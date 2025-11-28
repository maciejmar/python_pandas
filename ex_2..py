import random

'''gemerator liczb losowych'''
def losowe():
    for i in range(1000):
        yield random.randint(1,100)
gen = losowe()
print (f"losowa liczba = {next(gen)}")