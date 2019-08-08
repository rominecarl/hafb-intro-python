"""
Purpose: When working with iteratorw, generators, etc
look at the documentation for the itertools module
Day 4 AM 10:15
"""
from itertools import islice, count
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
    print("Are there prime numbers between 1328 and 1361", any(is_prime(x) for x in range(1328, 1362)))


if __name__ == "__main__":
    main()
    exit(0)