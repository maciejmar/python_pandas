''' how to do it is here: https://www.youtube.com/watch?v=U-G-mSd4KAE'''

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("you add sprinkles")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("you add fudge")
        func(*args,**kwargs)
    return wrapper
@add_fudge
@add_sprinkles
def serve_ice(flavour):
    print(f"here you have ice cream with {flavour} flavour")
ice_flavour="vanila"
serve_ice(ice_flavour)