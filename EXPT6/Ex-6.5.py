from functools import reduce

def ageCalc(a,b):
    return a+b

age = map(ageCalc, [1,2,3,6,9,44,8,4], [4,5,6,5,6,75,4,5])
    
def actualAge(x):
    return x+1

finalAge= reduce(actualAge, age)

adults = filter(lambda x: x>18, finalAge)

print(list(adults))