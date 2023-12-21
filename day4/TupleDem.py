# tuple () round brackets, creating tuple
mytuple = ("apple", 2.2, "frog", 'Cold', 'Yippee')
print(mytuple)
demotuple = ()
print(demotuple)
# accessing tuple items
print(mytuple[0])
print(mytuple[-1])
print(mytuple[1:3])
print(mytuple[:4:2])
print(mytuple[-3:-1])
# we cannot change tuple items as its immutable but..
# change tuple to list
litup = list(mytuple)
litup[0] = "selenium"
print(litup)
# change list to tuple
mytuple = tuple(litup)
print(mytuple)

# read items in tuple using loop
for i in mytuple:
    print(i)
# check item is present in tuple or not
if "Cold" in mytuple:
    print("present")
else:
    print("not")
# number of items in tuple
print(len(mytuple))

# adding items to tuple is not possible as it is immutable
# mytuple[0]="tom"
# print(mytuple)  # type error

# removing items from tuple is not possible as it is immutable
# del mytuple

# join / combine tuple using +
tuple1 = (10, 20, 30)
tuple2 = ("a", 'b', "c")
tuple3 = tuple1 + tuple2
print(tuple3)

# compare two tuple or list are equal or not
tuple4 = ('a', 'b', 'c')
if tuple1==tuple2:
    print("equal")
else:
    print("not equal")
if tuple4 == tuple2:
    print("equal")
else:
    print("not equal")