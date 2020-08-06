seq = "MLSSSMPPGGLACHADDDII"

d = {}

for i in seq:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
