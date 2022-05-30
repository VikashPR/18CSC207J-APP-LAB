def transformCase(string):
    return str(string).upper(), str(string).lower()


char = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

result = map(transformCase, char)

print(set(result))
