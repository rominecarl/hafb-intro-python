"""
Learn more about Python strings
"""


def main():
    """
    Test function
    :return: 
    """

    s1 = "This is super cool"
    print("size of string is: ", len(s1))

    # Concatenation "+"
    s2 = "Weber" + "State" + "University"
    print(s2)

    # For large strings, the join() method is recommended rather than "+"
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = ":".join(teams)    # First term is the separator
    print(record)

    # Split record - returns a list
    print("Split rec", record.split(":"))

    # Partitioning Strings - unpacks, need to provide sufficient values to catch
    # partition splits on the colon (or whatever) but also returns the colon
    # can use "_" if you don't care about the returned split parameter
    departure, separator, arrival = "London:Edinburg".partition(":")
    print(departure, arrival)

    dep, _, arr = "London:Edinburg".partition(":")
    print(dep, arr)
    t = "London:Edinburg".partition(":")
    print(t, type(t))
    #
    # String formatting using format()
    # can use a parameter multiple times
    print("The age of {0} is {1}".format("Mario",34))
    print("The age of {0} is {1}, and the birthday of {0} is {2}".format("Mario", 34, "August 12th"))

    # Omitting the index takes the parameters in order
    print('The best numbers are {} and {}'.format(4, 22))

    # By field name
    print("Current position {latitude}{longitude}".format(
        latitude="60 N", longitude="5E" ))

    # Print elements of list
    print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(
        pos=(85.6, 23.3, 99.0)  ))

    # # Second version of "format": print(f"{var}") python 3.7 or greater
    # # fname = "Waldo"
    # # lname = "Weber"
    # # print(f"The WSU mascot is {fname} {laname}")


if __name__ == "__main__":
    main()
    exit(0)