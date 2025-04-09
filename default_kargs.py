def abcd(name, age, District = "B. Baria", **kargs):
    print(name)
    print(age)
    print(District)
    print(kargs)
    for key, value in kargs.items():
        print(key, value)
    n = age*3
    return name, age, n # unlike c we can return more than one value in python. By default they will be return as tuple


X = abcd(age=23, name = "mahir", last = "tanzim", p = 2, r = 2)
print(X)