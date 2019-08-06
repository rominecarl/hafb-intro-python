"""
Learn about references
"""

def modify(k):
    """
    Modify the content of a list
    :param k:
    :return: nothing
    """

    # lists are passed by reference
    k.append(39)
    print("k = ", k)


def replace(g):
    """
    Replace input list
    :param g: input list
    :return: nothing
    """

    g = [17,48,89]  # <== this overwrites the list that was passed in as a reference. Probably not what you really wanted to do.
    print("g = ", g)

def main():
    """
    test function
    :return:
    """
    m = [9,15,24]
    print("Before: m = ", m)
    modify(m)
    print("After: m = ", m)
    replace(m)
    print("after replace() m = ", m)

if __name__ == '__main__':
    main()
    exit(0)