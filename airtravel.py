"""
Purpose: A Flight Class. Model for aircraft flights
Day 4 - 12:30
"""


class Flight:
    """
    A Flight with a particular passenger aircraft
    """

    # Python doesn't use the term constructor for technical reasons (nothing is actully constructed)
    # Python doesn't distinguish between public, private, friend, etc.
    def __init__(self, number):
        """
        Initializes flight number
        :param number: the flight number you want to initialize
        implementations details begin with '_'
        :raise: ValueError (For invalid format)
        """

        # Note, to be valid, a flight number has the format LL### i.e. 2 alpha characters followed by 3 numbers
        # Validate flight number: 5 chars long, AADDD A->ALPHA, D->Digit
        # Check for 5 chars long
        if len(number) != 5:
            raise ValueError("Invalid flight number length".format(number))

        # Check that 1st two characters are alpha
        if not number[:2].isalpha():
            raise ValueError("No airline code {}".format(number))

        # Check that 1st two characters are upper case
        if not number[:2].isupper():
            raise ValueError("Invalid Airline code [not uppercase: {}]".format(number))

        if not number[2:].isdigit():
            raise ValueError("Invalid route code {}".format(number))
        self._number = number  # single _ is python convention that this variable should be considered private. In reality you still have access

    def number(self):
        """
        Flight Number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        return self._number[:2]


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

        rows, seats = self.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows] # will hold the seating plan
        # will use letter as key in dictionary
        # "{letter:None for letter in seats}" will create a single dictionary
        # "for _ in rows" creates a dictionary for each row
        # we have a comprehension that is a list of comprehensions
        # this is using generators

        # these variables persist throughout the life of the object

    def allocate_seat(self, seat_number, passenger_name):


    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return(range(1, self._num_rows + 1),"ABCDEFGHJK"[:self._num_seats_per_row])
    # This method is using slicing. Need to investigate more
    # valid letters are: ABCDEFGHJKLMNPQRSTUVWXYZ <- NO I or O

def main():
    """
    Test function
    :return: 
    """
    pass


if __name__ == "__main__":
    main()
    exit(0)