

import time
start_time = time.time()
input='41078 18 7 0 4785508 535256 8154 447'
blinks=30
l=input.split()


#my code which works but slow
for _ in range(blinks):
    new_l = []  # Create a new list to hold the transformed stones
    for stone in l:
        # Rule 1: If the stone is '0', replace it with '1'
        if stone == '0':
            new_l.append('1')
        
        # Rule 2: If the stone has an even number of digits, split it into two stones
        elif len(stone) % 2 == 0:
            half_len = len(stone) // 2
            left_half = stone[:half_len]
            right_half = stone[half_len:]
            # Remove leading zeros from the right half if any
            right_half = right_half.lstrip('0')
            # If the right half is empty after stripping, just append '0'
            if right_half == '':
                right_half = '0'
            new_l.append(left_half)
            new_l.append(right_half)
        
        # Rule 3: If the stone doesn't meet the above rules, multiply it by 2024
        else:
            new_l.append(str(int(stone) * 2024))
    
    # Update the list with the transformed stones for the next blink
    l = new_l

# Output the final list after all blinks
print(len(l))
print(time.time()-start_time)
start_time = time.time()
input_str = '41078 18 7 0 4785508 535256 8154 447'
blinks = 30
l = input_str.split()
#this is also too slow next is parallel processing
# Function to handle each stone's transformation
def transform(stone):
    if stone == '0':
        return ['1']  # Rule 1
    elif len(stone) % 2 == 0:
        half_len = len(stone) // 2
        left_half = stone[:half_len]
        right_half = stone[half_len:].lstrip('0') or '0'  # Strip leading zeros, or '0' if empty
        return [left_half, right_half]  # Rule 2
    else:
        return [str(int(stone) * 2024)]  # Rule 3

# Efficiently transform stones for each blink
for _ in range(blinks):
    new_l = []  # Create a new list for the next blink
    for stone in l:
        new_l.extend(transform(stone))  # Extend list with the transformed stone(s)
    l = new_l  # Update the list for the next iteration

# Output the final list length
print(len(l))

print(time.time()-start_time)
import concurrent.futures
# Function to handle each stone's transformation
def transform(stone):
    if stone == '0':
        return ['1']  # Rule 1
    elif len(stone) % 2 == 0:
        half_len = len(stone) // 2
        left_half = stone[:half_len]
        right_half = stone[half_len:].lstrip('0') or '0'  # Strip leading zeros, or '0' if empty
        return [left_half, right_half]  # Rule 2
    else:
        return [str(int(stone) * 2024)]  # Rule 3

# Parallelized code to apply transformations
def parallel_processing(input_str, blinks):
    l = input_str.split()

    # Efficiently transform stones for each blink using parallel processing
    for _ in range(blinks):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Process the stones in parallel
            new_l = list(executor.map(transform, l))

        # Flatten the new_l list (since executor.map returns a list of lists)
        l = [item for sublist in new_l for item in sublist]

    return len(l)

# Input data
input_str = '41078 18 7 0 4785508 535256 8154 447'
blinks = 30
#still not enough 
# Measure time for parallel processing
start_time = time.time()
parallel_result = parallel_processing(input_str, blinks)
print(parallel_result)
print(time.time() - start_time)


start_time = time.time()
from functools import cache

line = '41078 18 7 0 4785508 535256 8154 447'
stones = []
for number in line.split():
    stones.append(int(number))

# Define a cached recursive function to count stones after a given number of steps
# we can do this since stones never merge so a certain node never touches its neighbour.
# faster because we cant get a very large number until we have to split it
# so we sortof make a lookup table for the answer thats already been computed after some time.
@cache
def process_stone(value, remaining_blinks):
    if remaining_blinks == 0:  # Base case: no blinks left
        return 1
    if value == 0:  # if stone is 0
        return process_stone(1, remaining_blinks - 1)
    
    value_str = str(value)
    length = len(value_str)
    
    if length % 2 == 0:  # if even digits
        midpoint = length // 2
        left_half = int(value_str[:midpoint])
        right_half = int(value_str[midpoint:])
        return process_stone(left_half, remaining_blinks - 1) + process_stone(right_half, remaining_blinks - 1)
    else:  # otherwise, multiply stone by 2024
        new_value = value * 2024
        return process_stone(new_value, remaining_blinks - 1)


total_stones = 0
for stone in stones: # for each stone we see how many they make
    total_stones += process_stone(stone, 30)

print(total_stones)
print(time.time() - start_time)
# n = total number of stones in the initial input (file size)
# d = average number of digits per stone in the input
# b = total number of blinks

# Time Complexity:
# Reading Input: O(n)
# Recursive Processing per Stone: O(b * d)
# Total Recursive Processing for All Stones: O(n * b * d)

# Space Complexity:
# Input Storage: O(n)
# Caching Storage: O(n * b)
# Call Stack Depth: O(b)
# Total: O(n * b)


