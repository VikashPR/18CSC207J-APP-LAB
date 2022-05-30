string = input("Enter a string: ").split()
numList = []


for i in string:
    if i.isdigit():
        numList.append(int(i))

length = int(len(numList))
numList = sorted(numList)

for i in (filter(lambda x: x > length, numList)):
    print(i, end=" ")
