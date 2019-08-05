"""
Learn dictionaries
Dictionaries maps keys to values.

In some languages are known as associative arrays, hashes, or maps.

Create using {} containing a key-value pair
Retrieve them by [key_value]

"""

#first item is the key, 2nd is the value
d = {'alice':'801-123-8988',
    'pedro':'956-445-78-8966',
    'john':'651-321-66-4477'}
print(d, type(d))
# Access one element
print(d['pedro'])

# add members to the dictionary, of names -> grades
roster = {}             # Empty dictionary
d['john'] = 7           # if entry already exists
d['tyler'] = 'bonehead' # if entry does not already exist, gets added

print(d)

names = {}
total = 0
while total <3:
    name = input("Enter a name: ")
    value = input("Enter a value: ")
    names[name] = value
    total = total + 1

print(names)
