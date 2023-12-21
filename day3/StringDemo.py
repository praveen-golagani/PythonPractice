s = "Welcome"
msg = str("Hello All")
game = 'Cricket'
game2 = "Hockey"
# declaring a string variable
place = str()
animal = ""
thing = ''

# string immutable
print(id(s))
s = s + "TO Python"
print(id(s))
p = "Welcome"
print(id(p))  # string is immutable

# + *
print(game + game2)
print(game * 3)

# Slicing []
print("prints from 0 index to n-1 ie 2nd index: " + game[0:3])
print("prints from 0 index to n-1 ie 5nd index: " + game[:6])
print("prints from 2 index to last index: " + game[2:])
print("prints from 1 index to n-1 ,but here -1 so n-2 ie 7-2 till 5th index: " + game[1:-1])
print("prints from 1 index to n-1 ,but here -2 so n-3 ie 7-3 till 4th index: " + game[1:-2])
print("this reverses complete string :" + game[::-1])

# ord() chr() for ascii and vice versa
print("ord() chr()")
print(ord('B'))
print(chr(66))

# max() min() len()
print("max() min() len()")
print(max("abc"))
print(min("abc"))
print(len("Praveen"))
print(len(game2))
print("length of :" + game + " is :" + str(len(game)))

# in, not in
print("in, not in")
print("ric" in game)
print("out" in game)
print("ric" not in game)
print("out" not in game)
print("rush20".isalnum())

# string comparison using relational operators
print("string comparison using relational operators")
print("Ant" > "")
print("apple" == "APPLE")
print("Free" != "Fire")
print("arrow" > "hell")
print("arrow" >= "arrow")
print("fbi" < "Fbi")
print("fbi" <= "fbi")

# testing strings
print("testing strings")
print("rush20".isalnum())
print("rush20".isalpha())
print("rush".isalpha())
print("rush20".isdigit())
print("20".isdigit())
print(s.isdigit())
print(s.isspace())
print(s.islower())
print(s.isupper())
print(" ".isspace())

# searching for substring
print("searching for substring")
fun = "welcome to python"
print(fun.endswith("on"))
print(fun.endswith("goal"))
print((fun.startswith("wel")))
print(fun.startswith("World"))
print(fun.find("come"))
print(fun.find("praveen"))
print(fun.count("o"))

# converting strings
print("converting strings")
print("converting strings".capitalize())
print(fun.capitalize())
s= "praveen gol"
cap = s.capitalize()
print(cap)
s2 = s.title()
print(s2)
print("string in python".title())
s3 = s.lower()
print(s3)
s4 = s.upper()
print(s4)
s5 = s.swapcase()
print(s5)
print("convRrting sTrings".swapcase())
s6 = s.replace("vee","VEE")
print(s6)


