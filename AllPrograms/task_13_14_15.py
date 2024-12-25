#task 13 - String - Group /collection/sequence of characters
message_1 = 'welcome'
message_2 = "praveen's test"    #apostrophe
message_3 = ''' interor's fun    
             message '''  #paragraph
print(message_1)
print(message_2)
print(message_3)
name = 'Python Life Best for Python learning'
num_str = '10'
print(f"Data type of num_str : {type(num_str)}") 
print(f"upper case : {name.upper()}") 
print(name.lower()) #lower case
print(name.count("Python")) #count of occurance
print(name.count('t'))
# print(name.index('fun'))  #returns error if string is not present
print(name.find('fun'))     #returns -1 if string is not present
print(name.startswith('P')) # startswith()
print(name.startswith('p'))
print(name.startswith("Life"))
print(name.endswith("Learning")) #endswith()
print(name.endswith("g"))
print(name.endswith("fun"))
websites = ["bikes.in","cars.com","ride.in","kart.com"]
ind_sites = []
# applying endswith and filtering
for i in websites:
    if i.endswith("in"):
        ind_sites.append(i)
print(ind_sites)
# format function
users_list = ["Praveen",'Vrushab','Lavanya','Mani']
for i in users_list:
    print("hii {}, have some cake on christmas".format(i))
#is alpha numeric can be alphabet/numeric/alphanumeric
alp_test = "1Prav"
alp_test2 = "45.2"
alp_test3 = "45"
print(alp_test.isalnum())
print(alp_test2.isalnum())
print(alp_test3.isalnum())
sp_strip = "        I am Testing this now   "
print(len(sp_strip))  
print(sp_strip.strip())  #strip spaces at ends
print(sp_strip+"ant")
print(sp_strip.lstrip()) #strip spaces in left end
print(sp_strip.rstrip())  #strip spaces in right end
book = "This is my book"
print(book.title())
print(book.replace("is","mine"))
print(book.replace("is","game",1))
fun_list = name.split(" ")
print(fun_list)
fun_strinbg = " ".join(fun_list) #conv list to string using join()
print(fun_strinbg)
fun_strinbg = "*".join(fun_list)
print(fun_strinbg)

#string paragraph replace() is with are, the with that
task_14 = '''This is a paragraph. The user is going to replace
            "is" with "are" and "the" with "that" and view the o/p.
            This is Sparta!!'''
          
result = (task_14.lower().replace("is","Are")).replace('the','that')
print(result)


