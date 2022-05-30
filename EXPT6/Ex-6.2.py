num = input("Enter the factorial number: ")


def factorial(num):
    if(num > 0):
        return num*factorial(num-1)
    else:
        return 1


factorial = factorial(int(num))
print(factorial)
