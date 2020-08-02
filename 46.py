seq = '11A2TG3TT000AT1A2G'


new_seq =""
for i in seq:
    if i.isalpha():
        new_seq += i
print(new_seq)
