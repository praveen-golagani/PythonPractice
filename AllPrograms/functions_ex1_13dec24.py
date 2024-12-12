# no parameters no return type
def greet_hi():
     print("Hii..")
     
# with parameters no return type
user_name = input("Enter your name : ")
def greet_name(user_name):
    print(f"Welcome to the code world {user_name}")
    
# with parameters with return type
choco = input("Enter your fav chocolate : ")
def fav_choco(choco):
     return f"{user_name}'s fav chocolate is {choco}!!"
 
# no parameters with return type
def exit_greetings():
    return f"Bye see you again {user_name}"

# calling methods
greet_hi()
greet_name(user_name)
print(fav_choco(choco))
print(exit_greetings())