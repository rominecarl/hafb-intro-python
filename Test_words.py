"""
Testing the code originally written in the words.py file. Working through the example again to see how they work
13 Aug 19
"""

def fetch_words():
    """
    Fetch the words  a sorted word list with word counts from a prespecified URL
    :return: None
    :print: Word list
    """

    from urllib.request import urlopen
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    count = 0
    data = {}
    with urlopen(file) as story:
        for line in story:                          # reads the file one line at a time
            words = line.decode('utf-8').split()    # parse the line into words. Split defaults to spaces
            for word in words:                      # read through the word dictionary
                if word in data:                    # test for existance. I.e. does the entry already exist in the dictionary
                    data[word] += 1
                else:                               # data not found
                    data[word] = 1
                count += 1
    print("Total number of words", count)
    print ("Total data", data)


def try_dict():
    my_dict = {}
    print(my_dict)
    my_dict[0] = "bubba"
    my_dict[2] = "gump"
    my_dict[5000] = "third entry"
    my_dict["test"] = "this was a test"
    print(my_dict)
    print(my_dict[5000])
    # Note, this test shows me that the "index" to a dictionary can be anything, not just an integer.

def main():
    """
    Test function
    :return: nothing
    """
#    fetch_words()
    try_dict()

if __name__ == "__main__":
    main()
    exit(0)