user_input = input("Enter a sentence : ")
result = ""
list_user_input = user_input.split(" ")

for i in range(len(list_user_input)):
    word = list_user_input[i]
    reverse_word = ""
    for j in range(len(word) - 1, -1, -1):
        reverse_word += word[j]
    result += reverse_word + " "

print(result.strip())
