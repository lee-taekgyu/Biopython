seq = 'AGTTTATAG'

for i in range(0, len(seq), 3):
    print(seq[i])

for i in seq[::3]:
    print(i)
