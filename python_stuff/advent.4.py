def d4p2(fileName):
    """
    Read the file and return the count of X-MAS patterns.
    """
    cnt = 0

    with open(fileName, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]  # Remove empty lines

        # Ensure all lines are of equal length
        max_len = max(len(line) for line in lines)
        lines = [line.ljust(max_len, '.') for line in lines]  # Pad shorter lines with dots (placeholder)

        rows, cols = len(lines), len(lines[0])

        # Loop through the grid, avoiding boundaries
        for i in range(1, rows - 1):  # Avoid edges
            for j in range(1, cols - 1):  # Avoid edges
                if lines[i][j] == 'A':  # Check only if the center is 'A'
                    # Diagonal checks
                    top_left = lines[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else '.'
                    bottom_right = lines[i + 1][j + 1] if i + 1 < rows and j + 1 < cols else '.'
                    top_right = lines[i - 1][j + 1] if i - 1 >= 0 and j + 1 < cols else '.'
                    bottom_left = lines[i + 1][j - 1] if i + 1 < rows and j - 1 >= 0 else '.'

                    # Check X-MAS patterns
                    if ((top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M')) and \
                       ((top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M')):
                        cnt += 1

    return cnt

print(d4p2('advent4.txt'))
