f = open("./read_sample.txt", 'r')
r = f.readlines()
f.close()

for s in r:
    print(s.strip())

with open("./read_sample.txt", 'r') as handle:
    for line in handle:
        print(line.strip())
