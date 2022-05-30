def avg(num):
    result = tuple(map(lambda x: sum(x) / int(len(x)), num))
    return result


n = [(12, 15, 16, 17, 19, 10)]

print(avg(n))
