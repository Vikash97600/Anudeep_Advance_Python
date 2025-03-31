# Generator in py are special type of function that allows you to create an iterable sequences of values
# A generator function returns a generator object, which can be used to generate the values one by one as
# you iterate over it.
#  generator does not store value in memory.

# ● return: Ends the function execution and returns a value. Once a function returns a value, it cannot return again.
# ● yield: Pauses the function execution, returning a value but maintaining the
# function’s state. The function can continue to yield additional values until it is
# exhausted.

#  generator does not store value in memory

# def count(num):
#     counter=1
#     while counter<=num:
#         yield counter
#         counter+=1

# gen=count(10)
# for i in gen:
#     print(i)

def infinitLoop(start=0):
    while True:
        yield start
        start+=1
gen=infinitLoop()
for i in range(5):
    print(next(gen))