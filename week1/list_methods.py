
numbers = [10, 30, 20, 40, 70, 90, 80, 50, 60]
numbers.append(100)
print(numbers)
numbers.insert(2, 25)
print(numbers)
if 25 in numbers:
    numbers.remove(25)

if 11 in numbers:
    numbers.remove(11)
print(numbers)
last = numbers.pop()
print(last, numbers)

if 11 in numbers:
    print(numbers.index(11))

numbers.sort(reverse=True)
print(numbers)