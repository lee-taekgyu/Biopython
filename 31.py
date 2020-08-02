seq = 'AGTTTATAG'

r_seq = seq[::-1]
reverse_comp = ""

for i in r_seq:
    if i == 'A':
        reverse_comp += 'T'
    elif i == 'T':
        reverse_comp += 'A' 
    elif i == 'C':
        reverse_comp += 'G' 
    elif i == 'G':
        reverse_comp += 'C'

print(reverse_comp) 
