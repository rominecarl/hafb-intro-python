"""
Strings and Collections
A string is a immutable sequence of Unicode code-points.
It is not an array of characters. If you "change" a new one is created and the old destroyed. Automatically

"""

print('This is a string')
print("This is a string too")

# Concatenation and Adjacent Strings
s1 = "First"
s2 = "Second"
print(s1+s2)
print(s1+' '+s2)

#Multi-line Strings and newlines
s3 = """This
is
a
multiline string"""
print(s3)
s4 = "This is\na multi-line\nstring"
print(s4)

# Support for backslash
s5 = "A\\in a string"
print(s5)