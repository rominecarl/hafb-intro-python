"""
Purpose: Use flight class
Day 4 - 12:30
"""
from airtravel import Flight, Aircraft

def main():
    """
    Test function
    :return: 
    """

    f = Flight("SN066")
    print(f, type(f))
    print(f.number())
    print(f.airline())
    # Could use: Flight.number(f) <-- no one uses this approach. just mentioned for reference

    # f2 = Flight("ab345")
    # print(f2.number())

    # f3 = Flight("AB352")
    # print(f3.number())

    a1 = Aircraft("G-EUP", "Airbus A319", num_rows=22, num_seats_per_row=6,)
    print(a1.registration(), a1.model())

if __name__ == "__main__":
    main()
    exit(0)