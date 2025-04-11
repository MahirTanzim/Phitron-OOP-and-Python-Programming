number = [1,2,3,4,5,6,6,1,3,4,2,5, 9]
print(number)
number = set(number)
print(number)
number.add(3)
number.add(8)
print(number)
number.remove(3)
print(number)
for i in number:
    print(i)
if 3 in number:
    print("Yes")
else:
    print("NO")

A = {1,2,3,4}
B = {1,3,4,5,6}
print(A&B)
print(A|B)