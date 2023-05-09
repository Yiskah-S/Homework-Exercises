# Write a function factorial that accepts an integer parameter n. It uses recursion to compute and return the value of n factorial (also written as n!).

# int = 5

def factorial(int):
    if int < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif int == 0:
        return 1

    return factorial(int-1) * int

# test = factorial(int)
# print(f"{test = }")




# Write a function reverse that accepts a string text as a parameter. It returns the reverse of text by reversing all characters in the string.

# str = "cat"

def reverse(str):
    if len(str) <= 1:
        return str
    else:
        return reverse(str[1:]) + str[0]

# test = reverse(str)
# print(f"{test = }")


# Write a function bunny that accepts an integer parameter count. count represents a number of bunnies and each bunny has two big floppy ears. 
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

# count = 3

def bunny(count): 
    if count == 0:
        return 0
    return bunny(count - 1) + 2
    
# test = bunny(count)
# print(f"{test = }")





# Write a function is_nested_parens that accepts a string parens of only parentheses. 
# It returns True if those parentheses are properly nested, and False if they are not. You may assume that no non-parenthesis characters will be passed to this function.

# parens = "((()))"

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[0] == '(' and parens[-1] == ')':
        return is_nested_parens(parens[1:-1])
    else:
        return False

# Empty string returning True is dumb, because it's not properly nested
# parens!
# It should be:
# def is_nested_parens(parens):
#     if len(parens) % 2 <= 1 or parens[0] != "(" or parens[-1] != ")":
#         return False
#     else:
#         return is_nested_parens(parens[1:-1]) if len(parens) > 2 else True

# And empty string should return False

# test = is_nested_parens(parens)
# print(f"{test = }")





# Write a function search that accepts an unsorted array of integers, array, and an integer value to find, query. 
# It returns True if query is found in array, and False otherwise. Make the algorithm recursive.
# Be sure to implement search using recursion.

# array = ["b", "c", "a"]
# array = ["a", "b", "c"]
# array = []
# query = "a"

# def search(array, query):
#     if len(array) == 0:
#         return False
#     elif query == array[0]:
#         return True
#     else:
#         return search(array[1:], query)

# def search(array, query):
#     if len(array) == 0:
#         return False
#     elif query == array[0] or query == array[-1]:
#         return True
#     else:
#         return search(array[1:-1], query)

def search(array, query):
    if len(array) == 0:
        return False
    # elif query == array[0] or query == array[-1]:
    #     return True
    elif len(array) == 1:
        return query == array[0]
    else:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        return search(left_half, query) or search(right_half, query)
    
# test = search(array, query)
# print(f"{test = }")



# Write a recursive function is_palindrome that accepts a string text as a parameter. It returns a boolean value indicating whether or not that string is a palindrome  .

text = "racecar"

def is_palindrome(text):
    pass


# Write a recursive function named digit_match. It accepts two non-negative integers as parameters. It returns the number of digits that match in the two integers.
# Two digits match if they are equal and have the same position relative to the end of the number (i.e. starting with the ones digit).
# In other words, the function should compare the last digits of each number, the second-to-last digits of each number, the third-to-last digits of each number, and so fort, counting how many pairs match.
# Example:
# First number: 1072503891
# Second number: 62530841
# Number of matches: 4
# Matching pairs: 2-2, 5-5, 8-8, 1-1

num1 = 1072503891
num2 = 62530841

def digit_match(num1, num2):
    pass