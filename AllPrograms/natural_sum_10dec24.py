natural_num = int(input("Enter a number : "))
i = 0
sum = 0

while i<=natural_num:
    sum+=i
    i+=1   #increment to avoid infinite loop
    
print(sum)