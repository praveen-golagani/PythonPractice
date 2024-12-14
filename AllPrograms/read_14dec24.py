#open  ("path")
file = open("read_write_test.txt")
# read contents of file and print it to view
# print(file.read())

for i in file.readlines():
    print(i)
    

#close
file.close()