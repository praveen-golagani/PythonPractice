natural_num = int(input("Enter a number : "))
i = 0
sum = 0

while i<=natural_num:
    sum+=i
    i+=1   #increment to avoid infinite loop
    
print(sum)

#using for loop
f_result = 0
for j in range(1,natural_num+1):
    f_result+=j
print(f_result)