#this code works but its sloww for sample cases but not for entire file
'''with open ('advent9.txt','r') as f:
    text=f.read().strip()
s=''
for i in range(len(text)):
    if i%2==0:
        s+=str(i//2)*int((text[i]))
    else:
        s+='.'*int(text[i])   
l=list(s)
for i in range(1, len(l) + 1):
    if l[-i].isdigit():  # Check if the rightmost character is a digit
        left_index = s.find(".")  # Find the first occurrence of `,`                  #88960367801
        if left_index != -1:  # Ensure `,` exists
            # Swap the digit at the rightmost with the `,` at the leftmost
            l[left_index], l[-i] = l[-i], l[left_index]
            s = ''.join(l)  # Convert the list back to a string after each swap
final=s[1:]+'.'
cnt=0
total=final.count('.')
for i in range(len(final)-total):
    cnt+=i*int(final[i])
print(cnt)
    
with open('advent9.txt', 'r') as f:
    text = f.read().strip()  # Remove trailing newline characters or spaces

# Generate the string `s` directly
s = []
for i, char in enumerate(text):
    if char.isdigit():
        count = int(char)
        if i % 2 == 0:  # For even indices, repeat the index (i // 2)
            s.append(str(i // 2) * count)
        else:  # For odd indices, repeat dots                          
            s.append('.' * count)
s = ''.join(s)

# Perform swapping
s_list = list(s)  # Convert to list for mutability
left_index = 0  # Start with the leftmost index

for i in range(len(s_list) - 1, -1, -1):  # Traverse from the right
    if s_list[i].isdigit():  # If it's a digit
        # Find the next available dot for swapping
        while left_index < len(s_list) and s_list[left_index] != '.':
            left_index += 1
        if left_index < len(s_list):  # Ensure there's a dot to swap
            s_list[left_index], s_list[i] = s_list[i], s_list[left_index]
            left_index += 1  # Move to the next dot

# Final adjustments
s = ''.join(s_list)
final = s[1:] + '.'

# Calculate `cnt` in a single pass
cnt = sum(i * int(final[i]) for i in range(len(final) - final.count('.')) if final[i].isdigit())

# Output results
print(cnt)'''
with open("advent9.txt", "r") as file:
    disk_map = file.read().strip()

# Parse the disk map into segments
disk_segments = []
for i in range(0, len(disk_map), 2):
    file_length = int(disk_map[i])
    free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
    disk_segments.append(("file", file_length))
    if free_length > 0:
        disk_segments.append(("free", free_length))

# Build disk representation
blocks = []
file_id = 0
for segment, length in disk_segments:
    if segment == "file":
        blocks.extend([file_id] * length)
        file_id += 1
    else:
        blocks.extend(["."] * length)

# Compact the disk
left_walker, right_walker = 0, len(blocks) - 1
while left_walker < right_walker:
    while left_walker < len(blocks) and blocks[left_walker] != ".":
        left_walker += 1
    while right_walker >= 0 and blocks[right_walker] == ".":
        right_walker -= 1
    if left_walker < right_walker:
        blocks[left_walker], blocks[right_walker] = blocks[right_walker], blocks[left_walker]

# Calculate checksum
checksum = 0
for i in range(len(blocks)):
    if blocks[i] != ".":
        checksum += i * blocks[i]

print(checksum)

# n = number of blocks in the disk (length of the blocks array / length of input file)

# Time Complexity:
# Building Representation:    O(n)
# Compacting Process:         O(n)
# Checksum Calculation:       O(n)
# Total:                      O(n)

# Space Complexity:
# Blocks Array:               O(n)
# Auxiliary Variables:        O(1)
# Total:                      O(n)
'''with open('advent9.txt', 'r') as f:
    text = f.read().strip()

# Generate the string `s` directly
s = []
for i, char in enumerate(text):
    if char.isdigit():
        count = int(char)
        if i % 2 == 0:  # For even indices, repeat the index (i // 2)
            s.append(str(i // 2) * count)
        else:  # For odd indices, repeat dots
            s.append('.' * count)
s = ''.join(s)

# Perform swapping
s_list = list(s)  # Convert to list for mutability
left_index = 0  # Start with the leftmost index

for i in range(len(s_list) - 1, -1, -1):  # Traverse from the right
    if s_list[i].isdigit():  # If it's a digit
        # Find the next available dot for swapping
        while left_index < len(s_list) and s_list[left_index] != '.':
            left_index += 1
        if left_index < len(s_list):  # Ensure there's a dot to swap                                  #88898052544
            s_list[left_index], s_list[i] = s_list[i], s_list[left_index]
            left_index += 1  # Move to the next dot

# Final adjustments
s = ''.join(s_list)
final = s[1:] + '.'  # Remove the first character and add a dot at the end

# Calculate `cnt` in a single pass
cnt = 0
dot_count = 0
for i, char in enumerate(final):
    if char == '.':
        dot_count += 1
    else:
        cnt += (i - dot_count) * int(char)

print(cnt)'''
#still too low
###part 2###
#initial plan count number of 0s 1s 2s .... then find length of .s then iterate and replace dots with numbers
with open("advent9.txt", "r") as file:
    disk_map = file.read().strip()

# Parse the disk map into segments
disk_segments = []
for i in range(0, len(disk_map), 2):
    file_length = int(disk_map[i])
    free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
    disk_segments.append(("file", file_length))
    if free_length > 0:
        disk_segments.append(("free", free_length))

# Build disk representation
blocks = []
file_positions = [] # Metadata for each file: its start position, length, and ID
file_id = 0
pos = 0
for segment, length in disk_segments:
    if segment == "file":
        blocks.extend([file_id] * length)
        file_positions.append((pos, length, file_id))
        pos += length
        file_id += 1
    else:
        blocks.extend([None] * length)
        pos += length

# Aggregate free spaces into list of tuples
free_spaces = []
current_pos = 0
while current_pos < len(blocks):
    if blocks[current_pos] is None:
        start = current_pos
        while current_pos < len(blocks) and blocks[current_pos] is None:
            current_pos += 1
        free_spaces.append((start, current_pos - start))
    current_pos += 1

# Move files to the leftmost valid space
file_count = len(file_positions)
space_count = len(free_spaces)
for file_index in range((file_count - 1), -1, -1):  # Iterate through file_positions in reverse order
    start_pos, file_size, file_id = file_positions[file_index]
    for space_index in range(space_count):  # Iterate through free_spaces normally
        space_pos, space_size = free_spaces[space_index]
        if space_pos < start_pos and file_size <= space_size:
            # Move the file
            for j in range(file_size):
                blocks[start_pos + j] = None
                blocks[space_pos + j] = file_id
            # Update free space
            free_spaces[space_index] = (space_pos + file_size, space_size - file_size)
            break


# Calculate checksum
checksum = 0
for i, block in enumerate(blocks):
    if block is not None:
        checksum += i * block

print(checksum)

# n = number of blocks in the disk (length of the blocks array / length of input file)

# Time Complexity:
# Parsing Disk Map:           O(n)
# Building Representation:    O(n)
# File Movement:              O(n^2) in the worst case due to nested iteration
# Checksum Calculation:       O(n)
# Total:                      O(n^2)

# Space Complexity:
# Blocks Array:               O(n)
# Auxiliary Variables:        O(n) (for file_positions)
# Total:                      O(n)
