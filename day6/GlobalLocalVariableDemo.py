glob_var = 20
var = 22
print(id(var))
def hap():
    print(glob_var)
    # var = 24
    global var
    var = 23
    print(var)
    print(id(var))
hap()
print(var)