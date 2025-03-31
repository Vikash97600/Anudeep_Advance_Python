def myDecorator(func):
    def wrapper(*args,**kwargs):
        print("Before calling the function")
        result=func(*args,**kwargs)
        print("After calling the function")
        return result
    return wrapper
@myDecorator
def greet(name):
    print(f"Hello {name}")

greet("Vikash")