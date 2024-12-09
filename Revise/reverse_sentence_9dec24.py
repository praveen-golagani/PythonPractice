#taking input from the user
user_sentence = input("Enter a sentence :")
#reverse without word position change
req_reverse = ""
#string to to list
split_sentence = user_sentence.split(" ")
#reverse 
for i in range(0,len(split_sentence),1):
    for j in range(len(split_sentence[i])-1,-1,-1):
        req_reverse+=(split_sentence[i])[j]
    req_reverse+=" "

print(req_reverse.strip())        
    
    
