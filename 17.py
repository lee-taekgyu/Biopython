f = open("./write_sample.txt", 'w')
f.write("Hello\n")
f.write("write_sample text file\n")
f.close()


write_string = "Hello lee\ndefinetly, You can do it\nDon't doubt"
with open("./write_sample.txt", 'w') as handle:
    handle.write(write_string)
