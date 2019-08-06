"""
Learn about scoping in Python
"""

count = 0   #global object

def show_count():
    """
    Show the current count
    :return: nothing
    """
    print(count)


def set_count(n):
#    count = n       # Python is creating a local variable. Goes out of scope upon return
    global count    #references the global variable "count"
    count = n
def main():
    """
    Test function
    :return: 
    """
    print("Before: ",show_count())
    set_count(5)
    print("After: ", show_count())


if __name__ == "__main__":
    main()
    exit(0)