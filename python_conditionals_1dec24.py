# program to print the character count in a string

demo_var = input("Enter a string in lower case : ")
num = 0
req_var = input("Enter a character to get count : ")

for i in demo_var:
    if i== req_var:
        num+=1

print(f"{req_var} occured time/times : {num}")
    
    
