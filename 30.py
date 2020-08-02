seq = 'AGTTTATAG'
new_seq = ""
print(type(new_seq))
for i in seq:
    if i == 'A':
        new_seq += "T"
    elif i == 'T':
        new_seq += "A"
    elif i == 'C':
        new_seq += "G"
    elif i == 'G':
        new_seq += 'C'
print(new_seq)

