"""
Learn about collections: Tuples, Strings, Range, List, Dictionaries, Sets
"""


def do_tuples():
    """
    Pracice tuples
    :return: nothing
    """

    # Immutable sequence of arbitrary objects
    # Use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size ", len(t))
    print("One member: ", t[0])  # by index notaton
    # To iterate over a tuple
    for item in t:
        print(item)

    # Single tuples
    t1 = (6,)  # single tuples, must end with comma
    print(t1, type(t1))

    # another way to create tuples
    # parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))


def min_max(items):
    """
    Return the minimum and maximum elements of a list
    :param items: collection
    :return: the minimum and maximum
    """

    return min(items), max(items)


def swap(obj1, obj2):
    """
    Swap value of objects
    :return:
    """
    return obj2, obj1


def main():
    """
    Test Tuples
    :return:
    """

    do_tuples()
    output = min_max([56, 76, 11, 12, 90])
    print("min", output[0])
    print("max", output[1])  # works but not not optimal since have to remember order

    # tuple unpacking
    lower, upper = min_max([56, 76, 11, 12, 90])
    print("min", lower)
    print("max", upper)

    # Swap values
    a = "jelly"
    b = "bean"
    print(a, b)
    a, b = swap(a, b)
    print(a, b)
    a, b = b, a  # This is another way to swap, without the need of a function
    print(a, b)

if __name__ == "__main__":
    main()
    exit(0)
