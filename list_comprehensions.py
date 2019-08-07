"""
Purpose: Understand List Comprehensions
Readable, expressive, and effective
Day 3 14:25
"""
from math import factorial, sqrt
from pprint import pprint as pp


def is_prime(num):
    """
    Determine if a number (num) is prime
    :param n: number to test
    :return: True if n is prime, false otherwise
    """
    if num < 2:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


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

    # Use list comprehension []
    info2 = [(len(str(factorial(x)))) for x in range(20)]   # performing list and loop in single line
    print(info2)
    print(info2, type(info2))

    # Use Set comprehensions: {}
    info3 = {len(str(factorial(x))) for x in range(200)}     # this will give unique values
    pp(info3)

    # Dictionary Comprehensions. Remember that keys must be unique
    nba_teams = {'jazz':'SLC', 'warriors':'OAKLAND', 'lakers':'LA'}
    pp(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # Filter predicates
    # e.g. want to know all of the numbers between 1 and 100 that are prime.
    primes = [x for x in range(1001) if is_prime(x)]     # applies the is_prime filter to each x from 1 to 100 and only keeps the True values
    pp(primes)
    print(len(primes), primes)



if __name__ == "__main__":
    main()
    exit(0)