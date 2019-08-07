"""
Purpose: Learn about dictionaries
Day 3 - 10:30
"""


def main():
    """
    Test function
    :return: 
    """
    # Create a dictionary of URLs
    urls = {
        "google": "www.google.com",
        "yahoo": "www.yahoo.com",
        "twitter": "www.twitter.com",
        "wsu": "weber.edu"
    }

    print(urls, type(urls))
    # Access by key: [key]
    print(urls["wsu"])

    #Build dict with dict() constructor
    # remember that the 1st element is the key and must be unique. If the same key is found, the value is overwritten
    names_age = [('Alice', 32), ('Mario', 23), ('Hugo', 21)]
    d = dict(names_age)
    print(d)

    # Another method
    phonetic = dict(a='alpha', b='bravo',c='charlie', d='delta')
    print(phonetic)

    # Make a copy
    e = phonetic.copy()     # Makes a deep copy. has its own reference but points to same memory until value changes
    print(e)

    # Updating a dictionary: update() method
    stocks = {'GOOG':891, 'AAPL':416, 'IBM':194}
    print(stocks)
    stocks.update({'GOOG':999, 'YHOO':2})   #update() useful when you already have a data set. Data is changed or added as required
    print (stocks)

    # Iteration. Default is by key value
    for key in stocks:
        print(key)
        print("{k} => {v}".format(k=key, v=stocks[key]))

    # Iterate by values
    for val in stocks.values():
        print("val = ", val)

    # Iterate by both key and value with: items
    for items in stocks.items():
        print(items)        # Returns a tuple. remember that you can unpack tuples
    for k,v in stocks.items():
        print(k,v)

    # Testing for membership
    print('GOOG' in stocks)
    print('WINDOWS' not in stocks)  # It is true that WINDOWS is not in stocks

    # Deleting: del keyword
    print(stocks)
    del stocks['YHOO']
    print(stocks)




if __name__ == "__main__":
    main()
    exit(0)