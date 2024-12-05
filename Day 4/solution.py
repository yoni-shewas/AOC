with open("data.txt", "r") as f:
    lines = f.readlines()
    data = [line.strip() for line in lines] 
    data = [list(row) for row in data]  

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

def check_direction(data, row, col, word, row_offset, col_offset):
    for k in range(len(word)):
        r = row + k * row_offset
        c = col + k * col_offset
     
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]) or data[r][c] != word[k]:
            return False
    return True


for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j].upper() == "X":  
            for row_offset, col_offset in directions:
                if check_direction(data, i, j, word, row_offset, col_offset):
                    count += 1

print(f"The word 'XMAS' was found {count} times.")
