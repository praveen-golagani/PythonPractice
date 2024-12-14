#write

with open("read_write_test.txt","r") as reader:
    content = reader.readlines()
    print(reversed(content))
    with open("read_write_test.txt","w") as writer :
        for i in reversed(content):
            writer.write(i)
            
