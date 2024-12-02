# taking input word from the user and reversing
word = input("Enter a senetence / word : ")
result = ""
word_count = len(word)

for i in range (word_count-1,-1,-1):
        result = result+word[i]

print(result)
