# 1. List Comprehension::Used to create lists in a single line.
# Syntax: [expression for item in iterable if condition]

squares=[x**2 for x in range(10)]
print(f"The squares of numbers from 0 to 9 using list comprenhension are: {squares}")

evenSquares=[x**2 for x in range(1,11) if x%2==0 ]
print(f"The even squares of numbers from 1 to 10 using list comprenhension are: {evenSquares}")

oddSquares=[x**2 for x in range(1,11) if x%2==1]
print(f"The odd squares of numbers from 1 to 10 using list comprenhension are: {oddSquares}")

pairs=[(x,x**2) for x in range(1,4)]
print(f"Number and its squares from 1 to 3 using list comprenhension are: {pairs}")

matrix=[[1,2,3],[4,5,6],[7,8,9]]
flattened=[element for row in matrix for element in row]
print(f"Elements of the matrix using list comprenhension are: {flattened}")

#WAP to find the prime number from 2 to 51
def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

primes=[x for x in range (2,51) if is_prime(x)]
print(primes)

#calculate discounted price using list comprenhension when aa the prices lists are given
prices=[120,85,150,30,70,200,95]
discounted_prices=[price*0.9 if price>100 else price for price in prices]
print(discounted_prices)

# 2. Set Comprehension: Used to create sets in a similar way to list comprehension.
# Syntax: {expression for item in iterable if condition}
'''
unique_squares = {x**2 for x in range(10)}
print(f"The unique squares of numbers from 0 to 9 using set comprenhension are: {unique_squares}")

'''
# 3. Dictionary Comprehension: Used to create dictionaries.
# Syntax: {key: value for item in iterable if condition}
'''
square_dict = {x: x**2 for x in range(10)}
print(f"The square dictionary of numbers from 0 to 9 using dictionary comprenhension are: {square_dict}")

'''
