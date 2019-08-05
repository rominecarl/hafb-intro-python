"""
Get a file from the Web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count number of words in document
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

