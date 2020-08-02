seq = 'AGTTTATAG'

count = {}

for i in seq:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1 
print(count)


import collections

A = collections.Counter(seq)
print(A)
