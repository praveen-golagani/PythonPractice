# keywords in python
import keyword

print(keyword.kwlist)
flag = False
f = "False"
num1 = 10
val = 4.5
listt = ['A', 1, 4, "Apple"]
tuplee = ('A', 1, 4, "Apple")
sett = {'A', 1, 4, "Apple"}
dictt = {"a": 33, 5: 12, 'tom': 245}
print("Data types : ", type(f), type(flag), type(num1), type(val), type(listt), type(tuplee), type(sett), type(dictt))

b = 57
act = "Sum"
cintrst = b + val
# %s for string, %d for numerics, %g for decimals
print("%s of %d, %d :" % (act, num1, b), num1 + b)
print("sum of : %g, %d is: %g" % (val, b, cintrst))
