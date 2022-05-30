test = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]
temp = [ele for sub in test for ele in sub]
result = list(zip(*temp))
print(str(result))