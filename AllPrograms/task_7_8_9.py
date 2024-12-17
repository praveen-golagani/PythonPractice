# task 7 - practice operators, conditional, jumping and looping statements
num1 = 48
num2 = 4    
num_add = num1+num2 # addition operator
num_diff = num1-num2 # subtraction operator
num_prod = num1*num2 # multiplication
num_div = num1/num2 # division
num_mod_div = num1%num2 # Modulus division
num_pow = num1**num2 # exponential
num_floor_div = num1//2 # floor division
print(f"Input values are {num1} and {num2} : ")
print(f"Operators Result- \nadditional:{num_add}\nsubtraction:{num_diff}\nmultiplication:{num_prod}\ndivision:{num_div}\nmodulo division:{num_mod_div}\nexponential:{num_pow}\nfloor division:{num_floor_div}")
#Comparision operators - prints boolean  - True/Flase
print(num1 > num2) #greater
print(num1 < num2) #less
print(num1 <= num2) #less than or equal
print(num1 >= num2) #greater than or equal
print(num1 == num2) # equal to, compares
print(num1 != num2) #not equal
print(f"and compares two booleans :  {4>2 and 2<3}")
print(f"using or: {4>2 or 2<1}") #if first condition is true it won't check next, else it checks

#Augment assignment operators
num3,num4,num5 = 7,4,8
num3 += num4 #Add and assign - o/p:11
print(num3) #print(num3+=num4) x syntax error as print doesnot support direct modification of var inside it
num5 -= 2 #subtract and assign - o/p:6
print(num5)
num3 *= 6 # multiply and assign - o/p: 66
print(num3)
num5 /= 3 # divide and assign - o/p: 2.0
print(int(num5)) #converted to int - 2
num3 //= 4 # floor divide and assign - o/p - 16
print(num3)
num4 **= 3 #exponentiate num4 and assign - o/p = 64
print(num4)

# conditionals - Flow control
#short hand if
user_id = int(input("Enter user id(>0) : ")) #taking input and conv to int
print(f"welcome user : {user_id}") if user_id>0 else print("Invalid user try later.")

# if elif else
num3,num4,num5 = 7,6,7
if num3>num4:
    if num3>num5:
        print(f"{num3} is greater")
    else:
        print(f"{num5} is greater ")
elif num4>num5:
    print(f"{num4} is greater")
elif num3==num4==num5:
    print("all are equal")
else:
    print(f"{num5} is greater")
    
# if else
num3,num4,num5 = 7,6,9
if num3==num4==num5:
    print("All are equal")
else:
    print(f"{max(num3,num4,num5)} is greater")
    
#looping and jumping 
word = input("Enter a word : ")
skip_letter = input("enter alphabet you want to skip printing : ")
result_word = ""
for i in word:
    if i==skip_letter:
        continue
    else:
        result_word+=i
        
print(f"skipped {skip_letter} in {word}, Result : {result_word}")

break_num = int(input("Enter a num b/w 1 to 10 : "))
# reverse print
for i in range(10,0,-1):
    if i == break_num:
        break
    else: print(i)

# 1 to 100 tables
for i in range(1,101):
    for j in range(1,11):
        print(f"{i} * {j} =  {i*j}")
 
training = "Python Life"
#without start point default is 0
for i in range(5):
    print(f"{i} . {training}")
#specify start point   
for i in range(1,6):
    print(f"{i} . {training}")
    
#odd num
trainer = "Kiran Sagar"
for i in range(1,9,2):
    print(f"{i} . {trainer}")

#while loop
marks = 90
while (marks<99):
    marks += 1
    if marks == 98:
        break
print(marks)


# login validation
user_name = "praveen"
password = "12345"
input_username = input("Enter username : ").lower()
input_pass = input("Enter Password : ")
# short hand if
print(f"welcome {user_name}") if input_username==user_name and password==input_pass else print("Invalid credentials")
