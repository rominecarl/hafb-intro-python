"""
Day 3 13:15
Purpose: Learn about sets
A set is an unordered collection of unique, immutable objects
Define using {}, just like a dictionary but no key needed
You can also use the set() constructor
"""


def main():
    """
    Test function
    :return: 
    """
    p = {6, 78, 21, 45}
    print(p, type(p))
    data = [1, 3, 5, 2, 88, 3, 1]
    print(data, type(data))
    # eliminate duplicates. Since a set can only contain unique objects, casting data to a set will quickly remove duplicates
    sdata = set(data)
    print(sdata, type(sdata))
    # Iterate with for
    for item in sdata:
        print(item)
    #Supports membership testing: in, not in
    print(5 in sdata)
    # update allows you to provide multiple values. Add uses a single value
    sdata.add(45)
    print(sdata)
    sdata.update([2, 99, 44, 1, 2, 88])
    print(sdata)

    # Removing elements
    sdata.remove(44)
    # sdata.remove(77)    #causes a key error since 77 does not exist in the data set
    print(sdata)
    # discard method does not raise an error if value is not present
    sdata.discard(77)
    print(sdata)

    #Copying sets
    bk_data = sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)
    ############ Define some sets
    blue_eyes = {"Olivia", "Harry", "Lily", "Jack"}
    blond_hair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
    smell_hcn = {"Harry", "Amelia"}
    taste_ptc = {"Harry", "Lily", "Amelia", "Lola"}
    o_blood = {"Mia","Joshua","Lily","Olvia"}
    b_blood = {"Amelia", "Jack"}
    a_blood = {"Harry"}
    ab_blood = {"Joshua", "Lola"}

    # Union: in any of the sets
    # Intersection: in all sets
    # symmetric difference: in only one set
    # subset: fully contained within a larger set
    # superset: has data in addition to another set

    print(blue_eyes.union(blond_hair))
    print(blue_eyes.intersection(taste_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blond_hair.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))




if __name__ == "__main__":
    main()
    exit(0)