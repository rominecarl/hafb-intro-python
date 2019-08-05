"""
Get a file from the Web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count number of words in document
"""

from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

count = 0
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()
        for word in words:
            count += 1
print("Total number of words", count)

