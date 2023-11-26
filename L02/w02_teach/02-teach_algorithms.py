"""
CSE212 
(c) BYU-Idaho
02-Teach - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

import timeit

def algorithm1(size):
    """
    The count variable is keeping track of the amount
    of work done in the function.  When the function is 
    done the count is returned.
    """
    count = 0
    for i in range(size): #O(n)
        count += 1
    return count

def algorithm2(size): #O(n^2)
    """
    The count variable is keeping track of the amount
    of work done in the function.  When the function is 
    done the count is returned.
    """
    count = 0
    for i in range(size):
        for j in range(size):
            count += 1
    return count

def algorithm3(size): # O(log(n))
    """
    The count variable is keeping track of the amount
    of work done in the function.  When the function is 
    done the count is returned.
    """
    count = 0
    start = 0
    end = size - 1
    while start <= end:
        middle = (end - start) // 2 + start
        start = middle + 1
        count += 1
    return count

""" 
    [1,2,3,4,5,6,7,8,9]
    [1,2,3,4]
    [3,4]
    [3]
"""
# This code will analyze the the 3 algorithms for different values of "n" (size of the data)
print("{:>15}{:>15}{:>15}{:>15}{:>15}{:>15}{:>15}".format("n","alg1-count","alg2-count","alg3-count","alg1-time","alg2-time","alg3-time"))
print("{:>15}{:>15}{:>15}{:>15}{:>15}{:>15}{:>15}".format("-"*10,"-"*10,"-"*10,"-"*10,"-"*10,"-"*10,"-"*10))
for n in range(0,10001,1000):
    count1 = algorithm1(n)
    count2 = algorithm2(n)
    count3 = algorithm3(n)
    time1 = timeit.timeit("algorithm1(n)", number=10, globals=globals()) / 10 * 1000
    time2 = timeit.timeit("algorithm2(n)", number=10, globals=globals()) / 10 * 1000
    time3 = timeit.timeit("algorithm3(n)", number=10, globals=globals()) / 10 * 1000
    print("{:>15}{:>15}{:>15}{:>15}{:>15.5f}{:>15.5f}{:>15.5f}".format(n, count1, count2, count3, time1, time2, time3))



