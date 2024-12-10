list_cart = ['Ironman',3,54.33,'a',"missile"]
#from starting to lastindex+1
print(list_cart[1:5])
print(list_cart[0:5:1])
print(list_cart)
#print list elements in reverse
print(f"Reversed list using index : {list_cart[::-1]}")
print(list_cart)
#reverse list using reverse()
list_cart.reverse()
print(f"reverse function : {list_cart}")
print(list_cart)
# list_cart.append("wolf","smart")  #we can append only one value
list_cart.append("wolf")
list_cart.append("smart")
#inserts at specific index
list_cart.insert(0,99)
print(list_cart)
# delete element at index
del list_cart[5]
print(list_cart)
