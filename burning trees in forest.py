#burning trees
"""input:6
0 1 1 1 0 1
0 1 0 1 0 0
1 0 1 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 1 0

position to fire:4,6
op:8"""
def spread_fire(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return

    matrix[i][j] = 0 
    spread_fire(matrix, i - 1, j) 
    spread_fire(matrix, i + 1, j)  
    spread_fire(matrix, i, j - 1)
    spread_fire(matrix, i, j + 1)  

def count_remaining_trees(matrix):
    count = 0
    for row in matrix:
        count += row.count(1)
    return count

def main():
    matrix = [
        [0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0]
    ]

    ignition_row, ignition_col = 4, 6
    spread_fire(matrix, ignition_row, ignition_col)
    remaining_trees = count_remaining_trees(matrix)
    print(f"{remaining_trees}")

if __name__ == "__main__":
    main()
    


