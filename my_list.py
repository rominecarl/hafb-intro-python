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
    t = s
    print(s)
    print(t)
    print("t is s:", t is s)
    t = s[:]
    print(s)
    print(t)
    print("t is s:", t is s)



if __name__ == "__main__":
    main()
    exit(0)