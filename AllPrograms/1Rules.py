# A variable name should start with a letter or the underscore character
name = "praveen"
_place = "India"

# cannot start with a number
# 2product = "chair"
# Variables are case sensitive
Name = "PRAVEEN"
NAME = "praveeng"
NAme = "gpraveen"
print(f"Name:{Name}\n name:{name}\n NAME:{NAME}\n NAme:{NAme}")
#Ids of the variables
print(f"Name:{id(Name)}\n name:{id(name)}\n NAME:{id(NAME)}\n NAme:{id(NAme)}")
user = "PRAVEEN"
#same data same address
print(f"same id  - Name:{id(Name)} user:{id(user)}")
# variable casing
'''
   Snake case - snake_case[Best]
   ex : user_name,product_cart
   camel case - camelCase
   ex: userName, productCart
   pascal case - PascalCase
   ex : UserName,ProductCart
'''

''' 35 keywords - False, None, True, and, assert, async, await, break, class, continue,
def, del, if,  elif, else, except, finally, for, from, global,import, in, is
lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
'''
