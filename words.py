"""
Get a file from the Web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

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

    # sort by keys
    for key in sorted(data.keys()):
        print(key, data[key])


def print_items(items):
    """
    Print elements of the collection
    :param items: A collections of objects
    :return: nothing
    """
    for item in items:
        print(item)


def main():
    """
    Test function
    :return: nothing
    """
    fetch_words()

if __name__ == "__main__":
    main()
    exit(0)

