"""
CSE212 
(c) BYU-Idaho
02-Teach - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def calc_factorial(n):
    """
    Calculate n! which equals n * (n-1) * (n-2) * ... * 2 * 1
    """
    factorial = 1
    for x in range(1, n+1):
        factorial *= x
    return factorial

# [a,b,c,d,e,f]
# O(n)

print(calc_factorial(4))  # Should print 24
print(calc_factorial(5))  # Should print 120

def calc_stats(numbers):
    """
    Determine and return the length of the numbers list, the sum
    of all the numbers, and the average of the numbers.
    """
    total_sum = 0
    count = 0
    for number in numbers: # O(n)
        total_sum += number
    for number in numbers: #O(n)
        count += 1
    avg = total_sum / count
    return count, total_sum, avg        
# O(n)+O(n) = O(2n)
# O(n)

print(calc_stats([1, 2, 3, 4, 5])) # Should print (5, 15, 3.0)
print(calc_stats([1, 2, 3])) # Should print (3, 6, 2.0)

def print_triangle(size):
    """
    Print a filled in isosceles  triangle to the screen.
    """
    for i in range(1, size+1): # O(n)
        for j in range(i): # O(n^2)
            print("*", end="")
        print()

#O(n)+O(n^2) = O(n^2)

""" 
1,2,3,4,5
*
**
***
****
*****
"""

print_triangle(5) # Print triangle with side length 5
print_triangle(8) # Print triangle with side length 5

# O(n^2)

def display_letters_in_names(names):
    """
    Display each letter of each name in the list on a separate line.
    """
    for name in names: #O(n)
        for letter in name: #O(3n)
            print(letter)

display_letters_in_names(["Bob","Sue","Tim"]) # Print out each letter one at a time

