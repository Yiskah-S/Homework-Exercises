# https://learn-2.galvanize.com/cohorts/3646/blocks/1829/content_files/hash-tables/overview-of-hash-tables.md
# Pseudocode
# With this strategy, our code will take this approach:

# Create a hash table (using a dictionary) that maps a number in an array to True, to show that it is present
# Create an empty list to hold all missing numbers
# For each number in the range between low and high, check the value in the map:
# If the number exists as a key in the dictionary, then the number is present
# If the number does not exist as a key in the dictionary, then the number is missing
# Append it to our list that holds all missing numbers

# Solution: Get Missing Numbers in Range

# Using Hash Tables
# Using a dictionary and the pseudocode above, implement get_missing_numbers_in_range.

# Here is the original prompt again:

# Write a function named get_missing_numbers_in_range. This function takes in an array of distinct integers, an integer low which is the lowest (inclusive) number in a range, and an integer high which is the highest (exclusive) number in a range.

# This function returns a list of all numbers that are between low (inclusive) and high (exclusive) and are not in array.

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

get_missing_numbers_in_range(array, low, high)

