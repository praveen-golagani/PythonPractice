name = "Praveen"
age = 30
salary = 89990.43
print(name, age, salary)
print("name is :", name)
print("age is: ", age)
print("name is %s Age is %d salary is %g" % (name, age, salary))
# Be careful below way
print("Name is {} Age is {} salary is {}".format(name, age, salary))
print("Name is {} Age is {} salary is {}".format(age, name, salary))

vijay = 20
print("{}{}".format("value is ",vijay))