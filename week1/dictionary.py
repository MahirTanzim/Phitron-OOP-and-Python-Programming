person = {'name': 'Mahir', 'age': 23, 'job': 'student'}
print(person)
print(type(person), len(person))
print(person['name'])
person['dept'] = "CSE"
print(person)

del person['age']
print(person)

for key, value in person.items():
    print(key+ " : "+ value)
