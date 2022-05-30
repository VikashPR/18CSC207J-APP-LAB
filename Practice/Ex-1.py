n = int(input("The total terms are: "))

result = list(map(lambda x: 5 ** x, range(n)))

for i in range(0, n):
    print("5 Power", i, "is", result[i])
