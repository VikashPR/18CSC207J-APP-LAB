from functools import reduce


def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


num = int(input("Enter the factorial number: "))
print(factorial(num))
