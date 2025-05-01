def double_decker():
    print("Outer Function")
    def inner_fun():
        print("Inner Function")
        return 23
    return inner_fun

# print(double_decker()())

def do(work):
    print("Do Something")
    work()
    print('asdf')

def code():
    print("Coding")
do(code)
