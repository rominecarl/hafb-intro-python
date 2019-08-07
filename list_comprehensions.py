"""
Purpose: Understand List Comprehensions
Readable, expressive, and effective
Day 3 14:25
"""
from math import factorial


def main():
    """
    Test function
    :return: 
    """
    words ="Today I am verry happy to learn about list comprehensions".split()
    print(words)
    data = []
    for word in words:      # this is what we've done so far
        # some analysis ...
        data.append(word)
        print(word)

    # Filter data - i.e. we finally have a list of data we care about in a form we can use

    # example: find the length of the first 20 factorial numbers, i.e. how many digits does each have?
    info = []
    # for x in range(20):
    #     #print(factorial(x))
    #     info.append(len(str(factorial(x))))
    #     print(info)

    # Use list comprehension
    info2 = [(len(str(factorial(x)))) for x in range(20)]   # performing list and loop in single line
    print(info2)
    print(info2, type(info2))

if __name__ == "__main__":
    main()
    exit(0)