# 1 check given number is positive or not
num = int(input("Enter num: "))
if num < 0:
    print("%d is negative" % (num))
else:
    print("%d is positive" % (num))
# 2 largest of 2 numbers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num1 > num2:
    print("%d is greater than %d" % (num1, num2))
elif num2 > num1:
    print("%d is greater than %d" % (num2, num1))
else:
    print("%d and %d are equal" % (num1, num2))
# 3 largest of 3
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
if num1 > num2 and num1 > num3:
    print("%d is largest of 3 numbers" % (num1))
elif num2 > num1 and num2 > num3:
    print("%d is largest of 3 numbers " % (num2))
elif num3 > num1 and num3 > num2:
    print("%d is greater of 3 numbers " % (num3))
else:
    print(" %d %d %d are equal" % (num1, num2, num3))

# 4 print week name as input print number
week_name = input("Enter starting 3 letters of weekday: ")
if week_name == 'MON':
    print(" day is : 1  num is : %s" % (week_name))
elif week_name == 'Tue':
    print("day is 2")
elif week_name == "Wed":
    print("day is 3")
elif week_name == "Thu":
    print("day is 4")
elif week_name == "Fri":
    print("day is 5")
elif week_name == "Sat":
    print("day is 6")
elif week_name == "Sun":
    print("day is 7")
else:
    print("Invalid entry")
