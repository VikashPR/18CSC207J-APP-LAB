n = int(input("Enter the size of the list: "))
list = []

for i in range(0, n):
    num = input()
    list.append(int(num))

listSum = sum(list)
listMax = max(list)

print("Sum of list elements is: ")
print(listSum)

print("Max of list elements: ")
print(listMax)
