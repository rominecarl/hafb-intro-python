"""
Learn Conditional Repetition
Two loops: for-loops and while-loops
"""

counter = 5
while counter != 0:
    print(counter)
    # Augmented Operator
    counter -= 1

counter = 5
while counter:
    print(counter)
    # Augmented Operator
    counter -= 1

#Break gets out of a loop
while True:
    print("Enter a number:")
    response = input()          #take user input
    if int(response) %7 == 0:   # number divisible by 7
        break                   # exit loop

print("outside while loop")