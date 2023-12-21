# key value pair " {}
mydiction = {101: "ant", 2: 'Z', 10: 22, "tom": 234}
mydiction1 = {'a': "mop", 1: 'z'}
print(mydiction)
print(mydiction1)
# num of items
val = len(mydiction1)
print("no of elements: ", val)
# accessing items from dict using key
print(mydiction1['a'])
print(mydiction[10])
# get() function
print(mydiction.get("tom"))
print(mydiction1.get("a"))
# change values
mydiction["tom"] = 121
print(mydiction)
# read items using loop
print("below prints only keys")
for i in mydiction:
    print(i)  # this prints only keys
print("below prints only values")
# way 1
for i in mydiction:
    print(mydiction[i])
print("way 2 values()")
for i in mydiction.values():
    print(i)

print("below as key values pair")
print("way 1 items()")
for x, y in mydiction.items():
    print(x, y)

print("way 2")
for i in mydiction:
    print(i, mydiction[i])

# check a key exists in dictionary
# way1
if 101 in mydiction:
    print("exist")
else:
    print("not")
# way2
print(101 in mydiction)

# adding items to dictionary
mydiction1["mahi"] = 7
print(mydiction1)
# copy into another
mydiction2 = mydiction1
print(mydiction2)
# way2 copy()
mydiction3 = mydiction.copy()
print(mydiction3)
# removing
mydiction3.pop("tom")
print(mydiction3)
del mydiction3[10]
print(mydiction3)
# del mydiction3
# mydiction3.clear()