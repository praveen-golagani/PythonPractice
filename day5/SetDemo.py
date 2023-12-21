# set {}
# creating set
myset = {"praveen", 1, 2.5, 'QA Engineer', 'A'}
print(myset)

# Accessing items from set
# print(myset[1]) # set is unindexed, unordered, no duplicate items
for i in myset:
    print(i)

# check item is present in set or not
# way1
if 2.5 in myset:
    print("present")
else:
    print("not")
# way2
print(2.5 in myset)
# Adding items to set
myset.add("python")  # single item at a time
myset.update(["programming", 2, 'z'])  # multiple items
print(myset)
print(len(myset))  # number of items in set

# union of two sets
myset1 = {"a", 'b', "c"}
myset2 = {1, 2, 3, 4}

myset3 = myset2.union(myset1)
print(myset3)
print(myset3.union(myset1))  # no duplication  they kind of overwritten
myset4 = {"Tom", "Flip"}
print(myset4)
# myset4 = myset4.update(myset2) # check this again
# print(myset4)

# remove() item from set
myset4.remove("Flip")
print(myset4)
# myset4.remove("Aussies")  # will return keyerror as item is unavailable
print(myset4)
myset.discard("praveen")
myset.discard("prav")  # will not return any error even if item is unavailable
print(myset)

# clear(), del
# myset.clear()
# del myset1
