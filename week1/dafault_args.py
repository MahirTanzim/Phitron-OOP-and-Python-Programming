
#args

def sum (a, b, *numbers):
    print(numbers)
    print(type(numbers))
    for n in numbers:
        print(n)

p = sum(1, 2, 3, 4, 4, 5)

# the values we pass to a function are stored as a tuple

def do_something(*args):
    print(args)
do_something(1,2,3,4,5,6,0)


