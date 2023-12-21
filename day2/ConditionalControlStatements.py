# if # if else # elif
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

# example 2
if True:
    print("True condition")
else:
    print("False condition")

# example 3
if False:
    print("condition 1")
else:
    print("condition 2")
# represents True, 0 represents False
if 1:
    print("con 1")
else:
    print("con 2")

if 0:
    print("con 0")
else:
    print("con")

# example4
num = 10
if num % 2 == 0:
    print("%d is even" % (num))
else:
    print("%d is odd" % (num))

# example 5
print("Even") if num % 2 == 0 else print("Odd")

# example 6
b = 5
{print("Hello"), print("Python")} if b == 10 else {print("Hi"), print("Java")}

# example 7
week = 5
if week == 1:
    print("Monday")
elif week == 2:
    print("Tue")
elif week == 3:
    print("wed")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Fri")
elif week == 6:
    print("Sat")
else:
    print("Invalid week")
