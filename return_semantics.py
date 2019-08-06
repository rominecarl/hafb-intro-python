"""
Learn about Python return semantics and how Python functions handle arguments
"""


def egg(var):
    """
    returns the variable back to the user
    :param var: input object
    :return: input object
    """

    return var


def sum_two(num1, num2=8):
    """
    Sum two imput objects
    :param num1: object 1
    :param num2: object 2 (optional, default = 8)
    :return: sum of objects
    """
    return num1 + num2


def banner(msg, boarder="*"):
    """
    print the message (input string) with
    :param msg: Text to display on banner
    :param boarder: optional character to create boarder from. Default = *
    :return: nothing
    """

    print(boarder * (len(msg)+4))
    print(boarder + " " + msg + " " + boarder)
    print(boarder * (len(msg) + 4))


def add_spam(menu=None):
    """
    Add spam to the menu list
    :param menu:
    :return: menu list
    """
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


def main():
    """
    Test function
    :return:
    """
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)

    n1 = 1.1003
    n2 = 9
    print(n1, " + ", n2, " = ", sum_two(n1, n2))
    print(n1, " + ", n2, " = ", sum_two(n1))

    banner("Bubba")
    banner("Gump", "#")
    banner("Weber State", "$")

    breakfast = ['eggs', 'bacon']
    snack = breakfast
    print("Before", breakfast)
    add_spam(breakfast)
    print("After", breakfast)
    print(breakfast is snack)


if __name__ == "__main__":
    main()
    exit(0)
