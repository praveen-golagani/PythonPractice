#Dictionary - key can be a string or int as well as value
dict_items = {"product_count": 22,
              5:"People",
              "Bill":245,
              "paid":True}
count = len(dict_items)
print(f" Items count : {count}")
#for loop in dict
print("--For loop---")
for i in dict_items:
        print(f" key : {i}, Value :{dict_items[i]}")
        
print("---Print values using values()---")
for i in dict_items.values():
    print(i)
    
    
print("----Using items()----")
for i,j in dict_items.items():
    print(i,j)
print("----if i don't use j ----")
for i in dict_items.items():
    print(i)
    
# using directly key and getting the value
print(dict_items["Bill"])
#using get method
print(f" using get method : {dict_items.get("paid")}")
# change value
dict_items["Bill"] = 2500
print(dict_items)

#check if a key exists returns Boolean
flag_item = "Bill" in dict_items
print(flag_item)

#way1 copy dict to another
dict_items1 = dict_items
print(f"dict items 1 : {dict_items1}")

#way2 using copy() function
dict_items2 = dict_items1.copy()
print(f"dict items 2 : {dict_items2}")

#del to delete a pair - use key
del dict_items2["paid"]
del dict_items1[5]
print(f"After del  - dict items 1 : {dict_items1}")
print(f"After del - dict items 2 : {dict_items2}")

# using pop(key)
print(f"Before pop - dict items  : {dict_items}")
dict_items.pop("product_count")
print(f"After pop - dict items  : {dict_items}")

#using clear()
print(f"Before clear - dict items2  : {dict_items2}")
dict_items2.clear()
print(f"After clear - dict items2  : {dict_items2}")

# adding items

dict_items2["car"] = "BE 6E"
print(dict_items2)