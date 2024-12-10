tuple_var = ('Ironman',3,54.33,'a',"missile")
#same as list , but tuple is immutable
# tuple_var[1]=33.33 #doesnot support item assignment
print(tuple_var)
#converted tuple to list
tuple_to_list = list(tuple_var)
# reassigned value
tuple_to_list[1]=33.33
print(tuple_to_list)
# list to tuple conversion
tuple_var = tuple(tuple_to_list)
print(tuple_var)
