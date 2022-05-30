
def sortString(n):
    sortedStr = sorted(n, key=lambda x: int(x))
    return sortedStr


str = []
num = int(input("Enter the length of the string: "))

for i in range(0, num):
    n = input()
    str.append(int(n))

print(sortString(str))
