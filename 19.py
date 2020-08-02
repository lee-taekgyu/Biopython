try:
    with open("noname.txt", 'r') as fr:
        read = fe.readline()
        print(read)
except FileNotFoundError:
    print("NO file")
