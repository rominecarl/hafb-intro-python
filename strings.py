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
print("this is ")

# Raw Strings
# tells python to take string as is, no escaping, or other processing
# string must start with an r
raw_string = r'c:\User\Documents\Books'
print(raw_string)

# String as sequence
# index notation starts at 0, processed like in other languages
s = "parrot"
print("s[4]", s[4], type(s))

print(s.capitalize())
g = s
print(g.capitalize())
g=s.upper()
print(g)
print(g[0])
