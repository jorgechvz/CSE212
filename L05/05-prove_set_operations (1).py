"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def intersection(set1, set2):
    """
    Perform an intersection between 2 sets.  An intersection will contain
    the items in common between both sets.  Do not use the set 
    operators (+, -, *, &, |) and functions (intersection, union) 
    that are built-in to Python.
    """
    intersection_set = set()  # Initialize an empty set to store the intersection
    for element in set1:
        if element in set2:
            intersection_set.add(element)  # Add common elements to the intersection set
    return intersection_set


def union(set1, set2):
    """
    Perform a union between 2 sets.  A union will contain all the items
    from both sets.   Do not use the set operators (+, -, *, &, |)
    and functions (intersection, union) that are built-in to Python.
    """
    union_set = set()  # Initialize an empty set to store the union
    for element in set1:
        union_set.add(element)  # Add elements from the first set
    for element in set2:
        union_set.add(element)  # Add elements from the second set (no duplicates will be added)
    return union_set

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(intersection(s1,s2))  # Should show {4, 5}
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8}
print("=======================")
s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10}
print(intersection(s1,s2))  # Should show an empty set
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

