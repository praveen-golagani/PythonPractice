values = [1, 2, "Ant", "K", 1.4]
#  list is a data type with multi values can be diff data type
print(values[0])

print(values[4])
print(values[-1])  # -1 specifies last index

print(values[1:3])  # exclusive last

values.insert(3, "Prav")
print(values)

values.append("End")
print(values)

values[2] = "PRAVEEN"  # UPDATING

del values[0]
print(values)
