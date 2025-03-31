def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator
    

@repeat(5)
def my_data():
    print("Python programming")

my_data()