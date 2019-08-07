"""
Purpose: Learn more about list()
Day 3 - 9:00
"""


def main():
    """
    Test function
    :return: 
    """
    # create a list
    s = "show how to do it".split()  # default splits on space
    print(s, type(s))

    # Access by index
    print(("s[3]", s[3]))

    print("s[3]:", s[3])    #unpythonic
    print("last member", s[len(s) - 1])

    # Better way - use negative index
    print("s[-1]:", s[-1])

    # Slicing
    # first number is starting point, 2nd number if included is up to but not included value
    print(s)
    print("From 1 to one before the last member", s[1:-1])
    print("From 1 to three members", s[1:3])
    print("From 1 to the end", s[1:])
    print("From beg to the 3", s[:3])
    print("From beginning to end", s[:]) # this creates a new list. Useful if making a deep copy.

    # Make a copy
    t = s   # both t and s point to the same memory location (shallow copy)
    print(s)
    print(t)
    print("t is s:", t is s)
    t = s[:]    # the contents of s is copied into t (deep copy)
    # t = s.copy()  - Alternative deep copy approach
    # t = list(s)   - Another alternative deep copy approach
    print(s)
    print(t)
    print("t is s:", t is s)    # should be false since separate memory locations
    print("t == s:", t == s)    # this should be true since the comparison operator checks values

    # Shallow copies
    # A list of lists
    a = [[1,2],[3,4]]
    print(a, type(a))
    print(a[0])
    print("a[0][1]:", a[0][1]) # way to access individual items
    # copy a list of lists
    # even when doing a deep copy, the values of both will point to the same memory. Only changes when element is changed
    b = a[:]
    print("a is b:", a is b)
    print("a == b", a == b)
    a[0] = [8,9]
    print("a is b:", a is b)
    print("a == b", a == b)
    print("a[0] is b[0]", a[0] is b[0])
    print("a[1] is b[1]", a[1] is b[1])
    # modify a[1]
    a[1].append(5)
    print("a[1]:", a[1])
    print("b[1]:", b[1])
    print("a[1] is b[1]", a[1] is b[1])
    print("a:", a)
    print("b:", b)

if __name__ == "__main__":
    main()
    exit(0)