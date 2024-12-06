def check_direction(data, row, col, word, row_offset, col_offset):
    for k in range(len(word)):
        r = row + k * row_offset
        c = col + k * col_offset
     
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]) or data[r][c] != word[k]:
            return False
    return True

def part1(data):

    count = 0 

    directions = [
        (0, 1),  
        (1, 0),   
        (1, 1),  
        (1, -1),
        (-1, 1),
        (-1, -1),
        (-1, 0),
        (0, -1)  
    ]

    word = "XMAS"  
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].upper() == "X":  
                for row_offset, col_offset in directions:
                    if check_direction(data, i, j, word, row_offset, col_offset):
                        count += 1
    return count

def check_x_mas(grid, row, col):
    n = len(grid)
    m = len(grid[0])

    # Check bounds for the X-MAS pattern
    if (
        row - 1 < 0 or row + 1 >= n or  # Check vertical bounds
        col - 1 < 0 or col + 1 >= m    # Check horizontal bounds
    ):
        return False

    # Top-left to bottom-right diagonal
    top_left_diag_valid = (
        grid[row - 1][col - 1].upper() == 'M' and
        grid[row][col].upper() == 'A' and
        grid[row + 1][col + 1].upper() == 'S'
    ) or (
        grid[row - 1][col - 1].upper() == 'S' and
        grid[row][col].upper() == 'A' and
        grid[row + 1][col + 1].upper() == 'M'
    )

    # Bottom-left to top-right diagonal
    bottom_left_diag_valid = (
        grid[row + 1][col - 1].upper() == 'M' and
        grid[row][col].upper() == 'A' and
        grid[row - 1][col + 1].upper() == 'S'
    ) or (
        grid[row + 1][col - 1].upper() == 'S' and
        grid[row][col].upper() == 'A' and
        grid[row - 1][col + 1].upper() == 'M'
    )

    # Check if both diagonals form an X-MAS
    return top_left_diag_valid and bottom_left_diag_valid

def part2(grid):

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].upper() == 'A':
                if check_x_mas(grid, i, j):
                    count += 1

    return count






def main():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        data = [line.strip() for line in lines] 
        data = [list(row) for row in data]

    print(f"The word 'XMAS' was found {part1(data)} times.") 
    print(f"The words 'XMAS' were found in the {part2(data)} times.") 



main()
