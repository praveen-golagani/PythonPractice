# single line comments
''' This is 
multi-line 
comments'''
string_var = "python life"


#type conversion float to int
num_float = 4.3
print(f" the data type of {num_float} is {type(num_float)}")
conv_float  = int(num_float)
print(f"upon conversion {conv_float} and type is {type(conv_float)}")

# taking input from the user
user_fav_num  = input("Enter your fav number : ")
print(f"the data type of {user_fav_num} is {type(user_fav_num)}")
# convert to int
int_fav_num = int(user_fav_num)
print(f"the data type of {int_fav_num} is {type(int_fav_num)}")

# convert to float
float_fav_num1 = float(int_fav_num)
float_fav_num2 = float(user_fav_num)
print(f"the data type of {float_fav_num1} is {type(float_fav_num1)})")
print(f"the data type of {float_fav_num2} is {type(float_fav_num2)})")

#task5 simple interest
principle = 15000
tenure = 6
rate = 2.2
SI = principle*tenure*rate/100
print(f" the simple interest is {SI}")