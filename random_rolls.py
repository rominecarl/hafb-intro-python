"""
Purpose: Simulate 6000 rolls of a die (1-6)
Day 3 12:30
"""
import random
import statistics

def roll_die(num):
    """
    Random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 maps to 1
    Index 1 maps to 2
    Index 2 maps to 3
    Index 3 maps to 4
    Index 4 maps to 5
    Index 5 maps to 6
    """
    freq = [0] * 6  # initialize list of frequencies
    for roll in range(num):
        n = random.randrange(1, 7)
        freq[n - 1] += 1

        # freq.append()
        # print(random.randrange(1, 7))
    return freq

def main():
    """
    Test function
    :return: 
    """
    num = int(input("How many times do you need to roll: "))
    result = roll_die(num)
    for roll, total in enumerate(result):
        print("Total rolls of {} = {}".format(roll +1, total))

    print("Average = {}".format(sum(result)/len(result)))
    print("Mean = {}".format(statistics.mean(result)))
    print("Median = {}".format(statistics.median(result)))

if __name__ == "__main__":
    main()
    exit(0)