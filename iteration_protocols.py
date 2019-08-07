"""
Purpose: Learn concepts of iterable, iterator objects
Use the built-in in:
iter(): create an iterable object
next(): fetch the next element in the iterable object
Day 3: 13:30
"""


def main():
    """
    Test function
    :return: 
    """
    iterable =["Spring", "Summer", "Fall", "Winter"]
    iterator = iter(iterable)
    print(type(iterator), iterator)


if __name__ == "__main__":
    main()
    exit(0)