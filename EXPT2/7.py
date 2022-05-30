number = [98,56,21,42,23,(52,78),40]
count = 0
for n in number:
    if isinstance(n, tuple):
        break
    count += 1
print(count)