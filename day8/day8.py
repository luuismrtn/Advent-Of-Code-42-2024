def main():
    file_path = 'input.txt'

    grid = []
    antinodes = set()

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                add_antinode(i, j, grid, antinodes)

    print("THE ANSWER IS:", len(antinodes))


def add_antinode(i, j, grid, antinodes):
    visited = set()
    letter = grid[i][j]
    visited.add((i, j))

    i_other, j_other = find_other(i, j, grid, letter, visited)

    while i_other is not None:
        visited.add((i_other, j_other))
        find_antinode(i, j, i_other, j_other, grid, antinodes)

        i, j = i_other, j_other
        i_other, j_other = find_other(i, j, grid, letter, visited)

def find_antinode(i, j, i_other, j_other, grid, antinodes):
    diff_i = abs(i - i_other)
    diff_j = abs(j - j_other)
    
    if i == i_other:
        an_i_1, an_j_1 = i, j - diff_j
        an_i_2, an_j_2 = i_other, j_other + diff_j
    
    elif j == j_other:
        an_i_1, an_j_1 = i - diff_i, j
        an_i_2, an_j_2 = i_other + diff_i, j_other
    
    else:
        if i < i_other and j > j_other:
            an_i_1 = i - diff_i
            an_j_1 = j + diff_j
            an_i_2 = i_other + diff_i
            an_j_2 = j_other - diff_j

        elif i < i_other and j < j_other:
            an_i_1 = i - diff_i
            an_j_1 = j - diff_j
            an_i_2 = i_other + diff_i
            an_j_2 = j_other + diff_j

        elif i > i_other and j < j_other:
            an_i_1 = i + diff_i
            an_j_1 = j - diff_j
            an_i_2 = i_other - diff_i
            an_j_2 = j_other + diff_j

        elif i > i_other and j > j_other:
            an_i_1 = i + diff_i
            an_j_1 = j + diff_j
            an_i_2 = i_other - diff_i
            an_j_2 = j_other - diff_j

    if 0 <= an_i_1 < len(grid) and 0 <= an_j_1 < len(grid[an_i_1]):
        antinodes.add((an_i_1, an_j_1))
    if 0 <= an_i_2 < len(grid) and 0 <= an_j_2 < len(grid[an_i_2]):
        antinodes.add((an_i_2, an_j_2))
    
    return antinodes

def find_other(i, j, grid, letter, visited):
    for i_other in range(len(grid)):
        for j_other in range(len(grid[i_other])):
            if grid[i_other][j_other] == letter and (i_other != i or j_other != j) and (i_other, j_other) not in visited:
                return i_other, j_other
    return None, None

if __name__ == "__main__":
    main()
