"""
Learn about Control Flow in Python
"""

# IF Statement
# Indentation is 4 spaces
if True:
    print("It is true")

print("Done")

if bool("eggs"):
    print("Yes please!")

if "eggs":
    print("Yes, why not")

#Flat is better than nested
h=42
if h > 50:
    print("Greater than 50")
    if h > 100:
        print("Greater than 100")
elif h < 50: #Else If
    print("Less than 50")
else:
    print("Equals 50")



#####
print("done")