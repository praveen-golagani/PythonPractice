# single line comments
''' This is  Task 4 
multi-line 
comments'''

#variables
#assigning same value to multiple var
speed1=speed2=speed3=200
print(f"values of speed 1 :{speed1}, speed2 :{speed2}, speed3:{speed3}")

#assigning multiple values to same variable
inflation = 4.5,10,12,9,2,10
print(f"inflation rates of diff countries : {inflation}")
print(type(inflation)) # tuple
inflation = 15
print(type(inflation)) #int
print(f"updated inflation is {inflation}")

#multiple values assigned to multiple variables respectively
bike2_speed,bike1_speed,car_speed = 45,60,100
print(f"car speed : {car_speed} kms/hr \n"
      f"first bike speed :{bike1_speed} kms/hr \n"
      f"second bike speed : {bike2_speed} kms/hr \n")

#type conversion float to int
num_float = 4.3
print(f"the data type of {num_float} is {type(num_float)}")
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

#task5  - wap on simple interest, CI
principal = 15000
tenure = 6
rate = 2.2
SI = principal*tenure*rate / 100
print(f"Task 5 - the simple interest is {SI:.2f}")  # format result to 2 decimals

# compound interest
total_amount = principal*(1+rate/100)**tenure
CI = total_amount - principal
print(f"the compound interest is {CI:.2f}")   # format result to 2 decimals

#task6 - write a python program on (a+b)**2
num1 = int(input("Task 6 - Enter first number : "))
num2 = int(input("Enter second number : "))
req_pow = int(input("Enter power : "))
result_pow = (num1+num2)**req_pow
print(f"power result : {result_pow}")