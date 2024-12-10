def main():
    file_path = 'input.txt'

    grid = []
    zeros_visited = set()
    total_sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            grid.append([int(x) for x in line])

    i, j = find_zero(grid, zeros_visited)
    while i is not None:
        zeros_visited.add((i, j))
        visited = set()
        paths_from_zero = set()
        find_path_recursive(i, j, grid, 0, visited, paths_from_zero)
        total_sum += len(paths_from_zero)
        i, j = find_zero(grid, zeros_visited)


    print("THE ANSWER IS:", total_sum)


def find_path_recursive(i, j, grid, num, visited, paths_from_zero):
    if (
        i < 0 or i >= len(grid) or 
        j < 0 or j >= len(grid[0]) or 
        (i, j) in visited or 
        grid[i][j] != num
    ):
        return

    if num == 9:
        paths_from_zero.add((i, j))
        return

    visited.add((i, j))

    find_path_recursive(i + 1, j, grid, num + 1, visited, paths_from_zero)
    find_path_recursive(i - 1, j, grid, num + 1, visited, paths_from_zero)
    find_path_recursive(i, j + 1, grid, num + 1, visited, paths_from_zero)
    find_path_recursive(i, j - 1, grid, num + 1, visited, paths_from_zero)

    visited.remove((i, j))


def find_zero(grid, zeros_visited):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and (i, j) not in zeros_visited:
                return i, j
    return None, None


if __name__ == "__main__":
    main()
