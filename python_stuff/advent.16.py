with open("advent16.txt", "r") as file:
    lines = file.readlines()
final_grid = [[""]*(len(lines)) for _ in range(len(lines[0]) - 1)]

moves = []
row = 0
for line in lines: #  format
    if "#" in line[0]:
        line = line.split("\n")[0]
        col = 0
        for i in line:
            final_grid[row][col] = i
            col += 1
        row += 1
    
# print(final_grid)

# Find start (S) and end (E) positions
start = None
end = None
for row in range(len(final_grid)):
    for col in range(len(final_grid[0])):
        if final_grid[row][col] == 'S':
            start = (row, col)
        elif final_grid[row][col] == 'E':
            end = (row, col)

# Directions: 0=North, 1=East, 2=South, 3=West
# Starting facing East as per problem statement
import heapq # Priority queue
directions = [(-1,0),(0,1),(1,0),(0,-1)]
start_state = (start[0], start[1], 1)  # row, col, direction

# Dijkstra's algorithm using a priority queue
dist = {}
dist[start_state] = 0
priority_queue = [(0, start_state)] # priority queue, keeps cheapest on top

while priority_queue:
    current_cost, (row, col, dir) = heapq.heappop(priority_queue)
    if (row, col) == end: # if no cheaper ways to get to end, solution found.
        print(current_cost)
        break
    if current_cost > dist[(row, col, dir)]:
        continue
    # Move forward
    new_row, new_col = row + directions[dir][0], col + directions[dir][1]
    if 0 <= new_row < len(final_grid) and 0 <= new_col < len(final_grid[0]) and final_grid[new_row][new_col] != '#':
        new_cost = current_cost + 1
        new_state = (new_row, new_col, dir)
        if new_state not in dist or new_cost < dist[new_state]:
            dist[new_state] = new_cost
            heapq.heappush(priority_queue, (new_cost, new_state))
    # Turn left
    new_dir = (dir - 1) % 4
    new_cost = current_cost + 1000
    new_state = (row, col, new_dir)
    if new_state not in dist or new_cost < dist[new_state]:
        dist[new_state] = new_cost
        heapq.heappush(priority_queue, (new_cost, new_state))
    # Turn right
    new_dir = (dir + 1) % 4
    new_cost = current_cost + 1000
    new_state = (row, col, new_dir)
    if new_state not in dist or new_cost < dist[new_state]:
        dist[new_state] = new_cost
        heapq.heappush(priority_queue, (new_cost, new_state))
    

# n = number of states processed (nodes explored in the priority queue)
# m = size of the grid (rows * columns)

# Time Complexity:
# Reading Input: O(m)
# Finding Start and End Positions: O(m)
# Dijkstra's Algorithm:
#   - Priority Queue Operations: O(n log n)
#     - Each state is pushed and popped from the queue once.
#   - State Transitions (forward, left, right): O(n)
# Total: O(m + n log n) so O(n log n)

# Space Complexity:
# Storing the Grid: O(m)
# Storing the Distances Dictionary: O(n)
# Storing the Priority Queue: O(n)
# Temporary Variables: O(1)
# Total: O(m + n)
with open("advent16.txt", "r") as file:
    lines = file.readlines()
final_grid = [[""]*(len(lines)) for _ in range(len(lines[0]) - 1)]

moves = []
row = 0
for line in lines: #  format
    if "#" in line[0]:
        line = line.split("\n")[0]
        col = 0
        for i in line:
            final_grid[row][col] = i
            col += 1
        row += 1
    
# print(final_grid)

# Find start (S) and end (E) positions
start = None
end = None
for row in range(len(final_grid)):
    for col in range(len(final_grid[0])):
        if final_grid[row][col] == 'S':
            start = (row, col)
        elif final_grid[row][col] == 'E':
            end = (row, col)

# Directions: 0=North, 1=East, 2=South, 3=West
# Starting facing East as per problem statement
import heapq # Priority queue
directions = [(-1,0),(0,1),(1,0),(0,-1)]
start_state = (start[0], start[1], 1)  # row, col, direction

# Track predecessors for backtracking
previous_states = {}

# Modified Dijkstra's algorithm to track all paths
distances = {}
distances[start_state] = 0
priority_queue = [(0, start_state)]
previous_states[start_state] = [] # useful when backtracking

while priority_queue:
    current_cost, (row, col, dir) = heapq.heappop(priority_queue)
    if distances[(row, col, dir)] < current_cost:
        continue
    # Move forward
    new_row, new_col = row + directions[dir][0], col + directions[dir][1]
    if 0 <= new_row < len(final_grid) and 0 <= new_col < len(final_grid[0]) and final_grid[new_row][new_col] != '#':
        new_cost = current_cost + 1
        new_state = (new_row, new_col, dir)
        if new_state not in distances or new_cost < distances[new_state]:
            distances[new_state] = new_cost
            heapq.heappush(priority_queue, (new_cost, new_state))
            previous_states[new_state] = [(row, col, dir)]
        elif new_cost == distances[new_state]:
            previous_states[new_state].append((row, col, dir))
    # Turn left
    new_dir = (dir - 1) % 4
    new_cost = current_cost + 1000
    new_state = (row, col, new_dir)
    if new_state not in distances or new_cost < distances[new_state]:
        distances[new_state] = new_cost
        heapq.heappush(priority_queue, (new_cost, new_state))
        previous_states[new_state] = [(row, col, dir)]
    elif new_cost == distances[new_state]:
        previous_states[new_state].append((row, col, dir))
    # Turn right
    new_dir = (dir + 1) % 4
    new_cost = current_cost + 1000
    new_state = (row, col, new_dir)
    if new_state not in distances or new_cost < distances[new_state]:
        distances[new_state] = new_cost
        heapq.heappush(priority_queue, (new_cost, new_state))
        previous_states[new_state] = [(row, col, dir)]
    elif new_cost == distances[new_state]:
        previous_states[new_state].append((row, col, dir))

# Backtrack to find all tiles part of the best paths
end_states = []
for state in distances:
    row, col, _ = state
    if (row, col) == end:
        end_states.append(state)
tiles_in_best_paths = set()

def backtrack(state):
    row, col, _ = state
    tiles_in_best_paths.add((row, col))
    for parent in previous_states.get(state, []): # in case it intersects, multiple parents.
        # get() avoids KeyError and returns empty list if not exist
        backtrack(parent)

for end_state in end_states:
    backtrack(end_state)

# Count tiles part of the best paths
best_path_count = len(tiles_in_best_paths)

print(best_path_count)



# n = number of states (nodes in priority queue)
# m = grid size (rows * columns)
# p = tiles in all best paths (unique tiles)

# Time Complexity:
# Reading Input: O(m)
# Finding Start/End: O(m)
# Dijkstra's Algorithm: O(n log n)
# Backtracking: O(p)
# Total: O(m + n log n + p) so O(n log n)

# Space Complexity:
# Grid Storage: O(m)
# Distances Dictionary: O(n)
# Priority Queue: O(n)
# Previous States: O(n)
# Best Path Tiles: O(p)
# Total: O(m + n + p)
