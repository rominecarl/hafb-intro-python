"""
Purpose: Learn about exceptions
Day 3 14:00
"""
import sys


def convert(s):
    """
    convert a string to integer
    :param s:
    :return:
    """

    try:
        return int(s)
    except (ValueError, TypeError) as e:        # the full information of the error found is packaged into an object we are calling e
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
    return -1


def sqrt(x):
    """
    Compute the square root using the method of Heron of Alexandria
    :param x: Number to compute the sqare root
    :return: The square root of x
    :raise  ValueError() on ZeroDivisionError
    """
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()  # sends error back to the

    return guess


def main():
    """
    Test function
    :return: 
    """
    # print(convert(11))          # works
    # print(convert("Hello"))     # throws error in original function
    # print(convert([1, 4, 8]))   # throws a different type of error (must be string, bytes-like

    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("Cannot compute the value of negative numbers")

    print("Done")


if __name__ == "__main__":
    main()
    exit(0)
