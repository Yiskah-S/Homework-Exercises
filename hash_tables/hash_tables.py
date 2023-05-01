#https://learn-2.galvanize.com/cohorts/3646/blocks/1829/content_files/hash-tables/using-hash-tables.md
# Pseudocode
# With this strategy, our code will take this approach:

# Create a hash table (using a dictionary) that maps a number in an array to True, to show 
# that it is present
# Create an empty list to hold all missing numbers
# For each number in the range between low and high, check the value in the map:
# If the number exists as a key in the dictionary, then the number is present
# If the number does not exist as a key in the dictionary, then the number is missing
# Append it to our list that holds all missing numbers

# Solution: Get Missing Numbers in Range

# Using Hash Tables
# Using a dictionary and the pseudocode above, implement get_missing_numbers_in_range.

# Here is the original prompt again:

# Write a function named get_missing_numbers_in_range. This function takes in an array of 
# distinct integers, an integer low which is the lowest (inclusive) number in a range, and 
# an integer high which is the highest (exclusive) number in a range.

# This function returns a list of all numbers that are between low (inclusive) and high 
# (exclusive) and are not in array.

# The missing elements should be returned in order they appeared in the original list.


array = [1, 14, 11, 51, 15]
low = 50	
high = 55

def get_missing_numbers_in_range(array, low, high):
    array_dict = {}
    return_list = []

    for num in set(array):
        array_dict[num] = True

    for num in range(low, high):
        if num not in array_dict:
            return_list.append(num)
    return return_list

# get_missing_numbers_in_range(array, low, high)

# Alternatives:

# def get_missing_numbers_in_range(array, low, high):
#     map = {}

#     for num in array:
#         map[num] = True

#     missing_nums = []
#     for i in range(low, high):
#         if i not in map:
#             missing_nums.append(i)

#     return missing_nums

# Pseudocode
# Our solution will take this approach:

# Create a hash table that maps every pair's first item to its second item
# Create an empty list to hold all symmetric pairs
# Iterate over the pair list again to ensure we process pairs in order:
# Check the hash table if the symmetric pair exists:
# Take the current second item, and use it as a key in the hash table
# Look up the value of the current second item in the hash table, and check whether its 
# value is equal to the current key (current first item)
# If it's equal, then there's a symmetric pair!
# Append it to our list of symmetric pairs
# Remove the current pair from the hash table so that it can't be matched by the symmetric 
# pair when we reach it in the list.
# Solution: Get Symmetric Pairs
# 2
# Using Hash Tables
# Using a dictionary and the pseudocode above, implement get_symmetric_pairs.

# Here is the original prompt again:

# Write a function named get_symmetric_pairs. This function takes in a list (pairs) of lists.
#  Each sub-list is a list of two elements.

# This function should return a list of all symmetric pairs. A pair should only be listed
#  once (without its symmetric counterpart).

# Assume that the first element of all pairs are distinct.

pairs = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]

def get_symmetric_pairs(pairs):
    symetric_pairs = []
    pairs_dict = {}

    for pair in pairs:
        pairs_dict[pair[1]] = pair[0]

        if pair[0] in pairs_dict and pairs_dict[pair[0]] == pair[1]:
            symetric_pairs.append([pair[1], pair[0]])

    return symetric_pairs

# Alternatives:

# get_symmetric_pairs(pairs)

# Solution given
# def get_symmetric_pairs(pairs):
#     pairs_map = {}

#     for pair in pairs:
#         pairs_map[pair[0]] = pair[1]

#     symmetric_pairs = []

#     for pair in pairs:
#         key, val = pair[0], pair[1]
#         if pairs_map.get(val) == key:
#             symmetric_pairs.append([key, val])
#             pairs_map.pop(key)

#     return symmetric_pairs

# https://learn-2.galvanize.com/cohorts/3646/blocks/1829/content_files/hash-tables/problem-set-hash-tables.md
# Write a function get_intersection that takes two integer lists with unique values and 
# returns their intersection in a new array.

# Be sure to use a dictionary in your solution. Do not use any built-in intersection functions.

red = [2, 3, 4]
blue = [4, 5, 6]

def get_intersection(red, blue):
    intersection = []
    red_dict = {}

    for num in red:
        red_dict[num] = True

    for num in blue:
        if num in red_dict:
            intersection.append(num)

    return intersection

# get_intersection(red, blue)

# Alternatives:

# def get_intersection(red, blue):
#     frequency_hash = {}

#     for list in [red, blue]:
#         for item in list:
#             if item in frequency_hash:
#                 frequency_hash[item] += 1
#             else:
#                 frequency_hash[item] = 1

#     intersections = []
#     for item, quantity in frequency_hash.items():
#         if quantity > 1:
#             intersections.append(item)

#     return intersections



# def get_intersection(red, blue):
#     frequency_hash = {}

#     for list in [red, blue]:
#         for item in list:
#             count = frequency_hash.get(item, 0)
#             frequency_hash[item] = count + 1

#     intersections = []
#     for item, quantity in frequency_hash.items():
#         if quantity > 1:
#             intersections.append(item)

#     return intersections

# Write a function is_permutation that takes two strings and returns True if one string 
# is a permutation of the other.

str1 = "hello"
str2 = "ehll"

def is_permutation(str1, str2):
    str1_dict = {}
    str2_dict = {}
    
    for char in str1:
        if char in str1_dict:
            str1_dict[char] +=1
        else:
            str1_dict[char] = 1

    for char in str2:
        if char not in str1_dict:
            return False
        else:
            if char in str2_dict:
                str2_dict[char] +=1
            else:
                str2_dict[char] = 1
    
    for key in str1_dict.keys():
        if str1_dict[key] != str2_dict.get(key):
            return False
        
    return True

is_permutation(str1, str2)

# Alternatives:

# def populate_frequency_map(text):
#     frequency_hash = {}
#     for char in text:
#         if char in frequency_hash:
#             frequency_hash[char] += 1
#         else:
#             frequency_hash[char] = 1
#     return frequency_hash


# def is_permutation(red, blue):
#     red_frequency_hash = populate_frequency_map(red)
#     blue_frequency_hash = populate_frequency_map(blue)

#     return red_frequency_hash == blue_frequency_hash



# def populate_frequency_map(text):
#     frequency_hash = {}
#     for char in text:
#         count = frequency_hash.get(char, 0)
#         frequency_hash[char] = count + 1
#     return frequency_hash


# def is_permutation(red, blue):
#     red_frequency_hash = populate_frequency_map(red)
#     blue_frequency_hash = populate_frequency_map(blue)

#     return red_frequency_hash == blue_frequency_hash

