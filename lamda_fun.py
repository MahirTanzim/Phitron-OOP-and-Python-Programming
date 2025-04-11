doubled = lambda num : num*2

print(doubled(3))

add = lambda x, y : x+y

print(add(1,33))

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)
# doubled_num = map(doubled, numbers)
# dn = list(doubled_num)
doubled_number = map(lambda n : n*2, numbers)
dn = list(doubled_number)
print(dn)
squared = map(lambda l : l**2, dn)
print(list(squared))

student = [
    {'name': 'mshir', 'age' : 24},
    {'name': 'billa', 'age' : 21},
    {'name': 'Rifat', 'age' : 20}
]
juniors = filter(lambda students : students['age'] < 23, student)

print(list(juniors))
