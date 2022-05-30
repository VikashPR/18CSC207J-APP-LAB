n = int(input("Enter the array size: "))
ageList = []
for i in range(0, n):
    age = input()
    ageList.append(int(age))

filterArray = list(filter(lambda x: x >= 18, ageList))

print(filterArray)
