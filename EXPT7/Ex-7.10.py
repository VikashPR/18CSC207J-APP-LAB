vowels = ['a', 'e', 'i', 'o', 'u']
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

vowelFilter = list(filter(lambda x: x in vowels, sequence))

print(vowelFilter)
