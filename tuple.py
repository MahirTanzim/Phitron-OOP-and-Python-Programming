def mul():
    return 3, 4

# x = mul()
# print(x, type(x))
things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'
print(things)
print(type(things))
print(things[2])
print(things[-3])
print(things[3:6])

if "phone" in things:
    print("YES")
for item in things:
    print(item)

print(len(things))