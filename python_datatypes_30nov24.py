num_var = 123987
name_var = "praveen"
deci_var = 12.34
t_boolean_var = True
f_boolean_var = False

#list allows multiple data type
list_items = ['Chocolate',"Apple",235,"dollars",'a',34.65]
print(list_items)
print(list_items[5])
print(type(list_items))

#tuple allows multiple

tuple_items = ('Chocolate',"Apple",235,"dollars",'a',34.65)
print(tuple_items)
print(tuple_items[5])

print(type(tuple_items))

#dictionary

dict_cart = {"item region":"usa", "item name" : "car", "item number":2965}
print(dict_cart["item name"])

#type

str_var = "healthy"
tuple_cart = ("healthy")
tuple_cart1 = ("healthy",)
print(f"the data type of {num_var} is {type(num_var)}")
print(f"the data type of {deci_var} is {type(deci_var)}")
      
print(f"the data type of {str_var} is {type(str_var)}")
#observe diff
print(tuple_cart)
print(f"the data type of tuple_cart is {type(tuple_cart)}")
print(tuple_cart1)
print(f"the data type of tuple_cart1 is {type(tuple_cart1)}")



