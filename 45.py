from random import randint
a = []
for i in range(6):
    n = randint(1,45)
    if n not in a:
        a.append(n)
for i in sorted(a):
    print(i)
