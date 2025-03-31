# Write a decorator that counts the number of times a function has been called.
from functools import wraps

def countCalls(func):
    count=0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} has been called {count} times")
        result=func(*args, **kwargs)
        return result
    return wrapper

@countCalls
def example_function():
    print("Function called")

# Example usage

example_function()
example_function()


        # or


# def call_counter(func):
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         print(f"{func._name_} has been called {wrapper.count} times.")
#         return func(*args, **kwargs)
#     wrapper.count = 0
#     return wrapper

# @call_counter
# def example_function():
#     print("Function executed")

# example_function()
# example_function()
# example_function()

