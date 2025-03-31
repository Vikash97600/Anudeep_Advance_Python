# gen=(x**2 for x in range(11))
# for num in gen:
#     print(num)

number=[1,2,3,4,5,6,7,8,9,10]
even=(num for num in number if num%2==0)
print(f"Even numbers from {number} are: ")
for e in even:
    print(e)

odd=(num for num in number if num%2==1)
print(f"Odd numbers from {number} are: ")
for o in odd:
    print(o)