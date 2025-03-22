import re
from sympy import symbols, Eq, linsolve
#wrong for some reason, i dont know why there is a slash in the output even if we divide its 40k
# Function to parse the text file and extract the necessary data
def parse_machine_data(file_path):
    machines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Temporary variables to store the current machine's data
        button_a_x = button_a_y = button_b_x = button_b_y = prize_x = prize_y = None
        
        # Loop through each line
        for line in lines:
            line = line.strip()
            if line.startswith("Button A"):
                # Extract button A movement data
                match = re.search(r"X\+(\d+), Y\+(\d+)", line)
                if match:
                    button_a_x, button_a_y = map(int, match.groups())
            elif line.startswith("Button B"):
                # Extract button B movement data
                match = re.search(r"X\+(\d+), Y\+(\d+)", line)
                if match:
                    button_b_x, button_b_y = map(int, match.groups())
            elif line.startswith("Prize"):
                # Extract prize location data
                match = re.search(r"X=(\d+), Y=(\d+)", line)
                if match:
                    prize_x, prize_y = map(int, match.groups())
                    # Once we have all data, append it to the machines list
                    machines.append((button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y))
    
    return machines

# Function to solve the system of equations for minimum cost to win a prize
def find_min_cost_to_win(prize_x, prize_y, a_x, a_y, b_x, b_y):
    # Define variables a and b (number of button presses for A and B)
    a, b = symbols('a b', integer=True)
    
    # Set up the system of equations
    eq1 = Eq(a * a_x + b * b_x, prize_x)  # X-axis equation
    eq2 = Eq(a * a_y + b * b_y, prize_y)  # Y-axis equation
    
    # Solve the system of equations
    solution = linsolve([eq1, eq2], a, b)
    
    # If the solution contains valid positive integers for a and b, return the cost
    for sol in solution:
        a_count, b_count = sol
        if a_count >= 0 and b_count >= 0 and a_count<=100 and b_count<=100:
            # Calculate the cost (3a + b)
            return 3 * a_count + b_count
    
    # If no valid solution found, return None
    return None

# Function to calculate the total cost of winning all prizes
def calculate_total_cost(machines):
    total_cost = 0
    total_prizes = 0

    for machine in machines:
        a_x, a_y, b_x, b_y, prize_x, prize_y = machine
        cost = find_min_cost_to_win(prize_x, prize_y, a_x, a_y, b_x, b_y)
        if cost is not None:
            total_cost += cost
            total_prizes += 1

    return total_prizes, total_cost

# Example Usage
file_path = 'advent13.txt'  # Path to the input file
machines = parse_machine_data(file_path)

# Calculate the total prizes won and total cost
total_prizes, total_cost = calculate_total_cost(machines)

# Output the results
print(f"Total prizes won: {total_prizes}")
print(f"Total cost: {total_cost}")
#i dont understand why gcd is used here even gpt said something using gcd
def gcd(a, b): # greatest common denominator
    while b != 0:
        a, b = b, a % b
    return a

def solve_machine(Ax, Ay, Bx, By, Px, Py):
    g1 = gcd(Ax, Bx)
    g2 = gcd(Ay, By)
    if Px % g1 != 0 or Py % g2 != 0:
        return None  # No solution possible


    B_max = min(100, Px // Bx) if Bx > 0 else 0
    for B in range(B_max, -1, -1):
        remaining_x = Px - Bx * B
        if Ax != 0 and remaining_x % Ax == 0:
            A = remaining_x // Ax
            if 0 <= A <= 100: # button pressed less then 100 times
                # Check Y equation
                if Ay * A + By * B == Py:
                    # Once we find a solution, it's the one with the most B's possible from this approach.
                    # We can return immediately.
                    cost = 3 * A + 1 * B
                    return cost

    return None


machines = []
with open("advent13.txt", "r") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    if lines[i].startswith("Button A:"):
        # Parse A line
        part = lines[i].split(",")
        Ax_str = part[0].split("X+")[-1].strip()
        Ay_str = part[1].split("Y+")[-1].strip()
        Ax = int(Ax_str)
        Ay = int(Ay_str)

        # Next line: Button B
        i += 1
        part = lines[i].split(",")
        Bx_str = part[0].split("X+")[-1].strip()
        By_str = part[1].split("Y+")[-1].strip()
        Bx = int(Bx_str)
        By = int(By_str)

        # Next line: Prize
        i += 1
        part = lines[i].split(",")
        Px_str = part[0].split("X=")[-1].strip()
        Py_str = part[1].split("Y=")[-1].strip()
        Px = int(Px_str)
        Py = int(Py_str)

        machines.append((Ax, Ay, Bx, By, Px, Py))
    
    i += 1

counter = 0
total_cost = 0
for (Ax, Ay, Bx, By, Px, Py) in machines:
    cost = solve_machine(Ax, Ay, Bx, By, Px, Py)
    print("Trying machine: ", counter, " amount ", cost)
    counter += 1
    if cost is not None:
        total_cost += cost

print(total_cost)


# Brute force approach, faster to implement, part2 has optimized approach.

# n = total number of machines

# Time Complexity:
# Reading Input: O(n)
# GCD Calculations: O(n)
# Iterating Over B for Each Machine: O(n * B_max), where B_max = min(100, Px // Bx)
# Total: O(n * B_max) so worst case O(100n) so O(n)

# Space Complexity:
# Storing Machines: O(n)
# Result Storage (solvable_costs): O(n)
# Temporary Variables: O(1)
# Total: O(n)
def solve_machine_optimized(Ax, Ay, Bx, By, Px, Py):
    Px += 10000000000000
    Py += 10000000000000

    denominator = Ax * By - Ay * Bx
    if denominator == 0:  # Division by 0 error later
        return None

    # Solve using the direct computation method
    i = (Px * By - Py * Bx) / denominator
    j = (Px - Ax * i) / Bx if Bx != 0 else 0  # Prevent division by zero again

    # Check if integers and above zero for it to be valid
    if i % 1 == 0 and j % 1 == 0 and \
    i >= 0 and j >= 0:
        cost = int(3 * i + 1 * j)  # Calculate total cost
        return cost

    return None


machines = []
# Read input from file
with open("advent13.txt", "r") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    if lines[i].startswith("Button A:"):
        # Parse A line
        part = lines[i].split(",")
        Ax_str = part[0].split("X+")[-1].strip()
        Ay_str = part[1].split("Y+")[-1].strip()
        Ax = int(Ax_str)
        Ay = int(Ay_str)

        # Next line: Button B
        i += 1
        part = lines[i].split(",")
        Bx_str = part[0].split("X+")[-1].strip()
        By_str = part[1].split("Y+")[-1].strip()
        Bx = int(Bx_str)
        By = int(By_str)

        # Next line: Prize
        i += 1
        part = lines[i].split(",")
        Px_str = part[0].split("X=")[-1].strip()
        Py_str = part[1].split("Y=")[-1].strip()
        Px = int(Px_str)
        Py = int(Py_str)

        machines.append((Ax, Ay, Bx, By, Px, Py))
    
    i += 1

counter = 0
total_cost = 0
for (Ax, Ay, Bx, By, Px, Py) in machines:
    cost = solve_machine_optimized(Ax, Ay, Bx, By, Px, Py)
    print("Trying machine: ", counter, " amount ", cost)
    counter += 1
    if cost is not None:
        total_cost += cost

print(total_cost)


# n = total number of machines, less than total number of lines.

# Time Complexity:
# Reading Input:               O(n)
# Solve Machine Calculations:  O(n)
# Total:                       O(n)

# Space Complexity:
# Storing Machines:            O(n)
# Temporary Variables:         O(1)
# Total:                       O(n)
