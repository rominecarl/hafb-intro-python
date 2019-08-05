"""
Practice for loops
Keyword: for
Python uses for each. parses through list and processes each element. No need to keep track of indexes etc

"""

cities = ["London", "New York","Madrid", "Paris", "Ogden"]
# iterate over the collection

for city in cities:
    print(city)

#first item is the key, 2nd is the value
d = {'alice':'801-123-8988',
    'pedro':'956-445-78-8966',
    'john':'651-321-66-4477'}

#iterate over a dictionary
for item in d:
        print(item)                     # by default a for loop processes the key of a dictionary
        print(item, "=>", d[item])      # use the key to point to the element within the dictionary

