"""
Learn about functions/definitions. Python uses the term definitions
Use the keyword: def <name>():
"""


def even_or_odd(number):
    """
    Find if number is even or odd
    :param number: input number
    :print "even" on even numbers
             "odd" on odd numbers
    """
    #pass                # dummy statement. each function requires at least one statement
    if number %2 == 0:
        print("even")
    else:
        print("odd")

def main():
    """
    Test function
    :return: nothing
    """

    if __name__ == "__main__":
        main()
        exit(0)
# Call function
    print(__name__)         # prints the name of the module
    even_or_odd(89)
    even_or_odd(22)

