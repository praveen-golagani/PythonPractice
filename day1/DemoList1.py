fruits = ["Apple", 'Banana', 'lEMON', 2, 56, 3.6, 'D', 2]

print(fruits[0])
print(fruits)
print(fruits[7])
print(fruits[-1])  # -1 specifies last index
fruits.append("Praveen")
print(fruits)
fruits.insert(2, 3)
print(fruits)
print(fruits[1:4])  # exclusive last
fruits.insert(2, "Lemon")
print(fruits)
fruits.remove(2)  # removed first occurrence of 2
print(fruits)
del fruits[8]  # deleted value at index 8
print(fruits)
