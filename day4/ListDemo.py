# list [] square brackets
# empty list creation, my_empty = list()
mylist = [10, 2, 3, 40, 44, 31]
# no of items in list
print("size of list :",len(mylist))
mylist3 = ["praveen", 10, 3.4, 44, 'Ani']
# Printing values from list
print("Printing values from list")
print(mylist)
print(mylist3)
print(mylist[0])
print(mylist3[2])
print(mylist[-1])
print(mylist[-2])
# printing items from a range of index
print(mylist3[1:4])
print(mylist[-4:-1])
# print(mylist[-1:-4])
print(mylist3[:5:2])
# change item values from list
mylist[0] = "tommy"
print(mylist)
# add item to list 2 ways append() insert()
print(mylist3)
mylist3.append("python")
mylist3.insert(2, "zombie")
print(mylist3)
# read items in list using loop
print("read items in list using loop")
for i in mylist:
    print(i)
# check an item exists in list or not
if 44 in mylist:
    print("True")
else:
    print("False")
# mylist3
if "Ani" in mylist3:
    print("True")
else:
    print("False")
# total number of items in list len()
print(len(mylist3))
# remove items from list. Its possible only through index using pop() method and del keyword
print(mylist3)
mylist3.pop(4)
print(mylist3)
del mylist3[3]
print(mylist3)
# mylist3.clear() # completely clears
# copy one list to some other list using list() and copy()
demolist = ["mona", 'tina', 1]
nlist = list(demolist)
print(nlist)
clist = demolist.copy()
print(clist)
# join 2 lists using +, append(), extend()
l1 = [1, 2, "fun"]
l2 = ["too", "long"]
l3 = l1 + l2
print(l3)
# append()
for i in l2:
    l3.append(i)
print(l3)
# extend()
l2.extend(l1)
print(l2)
