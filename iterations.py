"""
Purpose: When working with iteratorw, generators, etc
look at the documentation for the itertools module
Day 4 AM 10:15
"""
from itertools import islice, count, chain
from list_comprehensions import is_prime

def main():
    """
    Test function
    :return: 
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("List of the first 1K prime numbers:", list(thousand_primes))
    # Note: If you need to use the object again you need to re-generate it
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of the first 1K prime numbers:", sum(thousand_primes))

    # Other built-ins use with itertools: any, all
    print(any([False, False, True]))    # like an OR
    print(all([False, False, True]))    # like an AND

    # Want to find if there are any prime numbers in the range: 1328-1361
    # sub_prime = islice(x for x in range(1328,1363)) <-- this way my attempt
    print("Are there prime numbers between 1328 and 1361", any(is_prime(x) for x in range(1328, 1362)), list(x for x in range(1328, 1362) if is_prime(x)))

    # Check if all names in an iterable are in title form: i.e. First letter capitalized
    names = ["London", "New York", "Ogden"]
    print(all(name == name.title() for name in names))

    # Another built-in: zip()
    sunday  = [2, 2, 5, 7, 9, 10, 9, 6, 4, 4]
    monday  = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9]
    tuesday = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12]

    for item in zip(monday, tuesday):
        print(item)
    # Want to know the average temp for each set of readings, i.e. the average of the first monday temp and first tuesday temp, etc.
    for mon, tue in zip(monday, tuesday):
        print("average =", (mon + tue)/2)

    # Calculate the minimum, maximum, and average of all points
    # 4 = total width of the field (including decimal point), 1 = precision, f = floating point
    for temps in zip(sunday, monday, tuesday):
        print("min={:4.1f}, max={:4.1f}, avg={:4.1f}".format(min(temps), max(temps), sum(temps)/len(temps)))

    # chain
    all_temps = chain(sunday, monday, tuesday)
    print("All temperatures > 0:", all(t > 0 for t in all_temps))


if __name__ == "__main__":
    main()
    exit(0)