from functools import reduce


def fib(n): return reduce(lambda x, _: x+[x[-1]+x[-2]],
                          range(n-2), [0, 1])


print(fib(5))
