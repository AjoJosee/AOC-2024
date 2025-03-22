import re

# Function to handle the instructions and compute the result
def process_instructions(text):
    # Regular expression to match valid mul instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'  # Matches mul(X,Y) where X and Y are 1-3 digits
    do_pattern = r'do\(\)'  # Matches do() instruction
    dont_pattern = r"don't\(\)"  # Matches don't() instruction

    # To track the state of multiplication instructions
    enabled = True
    total = 0

    # First, we'll process all 'mul', 'do', 'don't' instructions while scanning the text
    index = 0
    while index < len(text):
        # Check for 'mul(X, Y)' instruction
        mul_match = re.match(mul_pattern, text[index:])
        if mul_match:
            if enabled:
                # Extract numbers from mul(X, Y) and compute the product
                x, y = map(int, mul_match.groups())
                total += x * y
            index += len(mul_match.group(0))  # Move the index past the current 'mul' instruction
            continue

        # Check for 'do()' instruction to enable mul()
        do_match = re.match(do_pattern, text[index:])
        if do_match:
            enabled = True
            index += len(do_match.group(0))  # Move the index past 'do()'
            continue

        # Check for 'don't()' instruction to disable mul()
        dont_match = re.match(dont_pattern, text[index:])
        if dont_match:
            enabled = False
            index += len(dont_match.group(0))  # Move the index past 'don't()'
            continue

        # Move to the next character if no match was found
        index += 1

    return total

# Read the input text from a file
with open('advent3.txt', 'r') as f:
    text = f.read()

# Process the text and print the result
result = process_instructions(text)
print(result)


