#I AM PROUD OF GETTING THIS INSTANTLY
with open('advent7.txt', 'r') as f:
    l = []
    for line in f:  # Iterate line by line
        l.append(line.strip().split(':'))

text = []
for item in l:
    key = int(item[0])  # Convert the first element to an integer
    values = list(map(int, item[1].strip().split()))  # Process the second element
    text.append([key, values])

from itertools import product

def evaluate_expression(numbers, operators):
    operator_combinations = list(product(operators, repeat=len(numbers) - 1))
    results = []
    
    for ops in operator_combinations:
        result = numbers[0]  # Start with the first number
        for i in range(1, len(numbers)):
            if ops[i - 1] == '+':
                result += numbers[i]
            elif ops[i - 1] == '*':
                result *= numbers[i]
            elif ops[i-1]=='||':
                result = int(str(result) + str(numbers[i]))
        results.append(result)
    
    return results
possible=[]
operators = ['+', '*','||']
for i in text:
    numbers = i[1]
    all_results = evaluate_expression(numbers, operators)
    possible.append(all_results)
count=0
for i in range(len(text)):
    if text[i][0] in possible[i]:
        count+=text[i][0]
print(count)
    
