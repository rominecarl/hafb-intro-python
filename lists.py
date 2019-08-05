"""
Learn about lists
Unlike strings, lists are mutable.
You can update and append elements to a list
"""

# use brackets [] to define a list
mylist = [1,2,3]
print("List ", mylist, type(mylist))

#you can have a list of any type. It is a list of objects
a = ["apple","orange","pear"]
# Access by index notation
print(a,a[1])
a[0]="tomatoes"
print(a,a[1])
a[1]=3.14
print(a, a[1])

# Begin with an empty list
total = 0
names = []
while total < 3:
    name = input("Enter a name: ")
    names.append(name)
    total = total + 1

print(names)

