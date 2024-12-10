def main():
    file_path = 'input.txt'

    grid = []
    zeros_visited = set()
    total_sum = [0]

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            grid.append([int(x) for x in line])

    i, j = find_zero(grid, zeros_visited)
    while i is not None:
        zeros_visited.add((i, j))
        find_path_recursive(i, j, grid, 0, set(), total_sum)
        i, j = find_zero(grid, zeros_visited)

    print("THE ANSWER IS:", total_sum[0])


def find_path_recursive(i, j, grid, num, visited, total_sum):
    if (
        i < 0 or i >= len(grid) or 
        j < 0 or j >= len(grid[0]) or 
        (i, j) in visited or 
        grid[i][j] != num
    ):
        return

    if num == 9:
        total_sum[0] += 1
        return

    visited.add((i, j))

    find_path_recursive(i + 1, j, grid, num + 1, visited, total_sum)
    find_path_recursive(i - 1, j, grid, num + 1, visited, total_sum)
    find_path_recursive(i, j + 1, grid, num + 1, visited, total_sum)
    find_path_recursive(i, j - 1, grid, num + 1, visited, total_sum)

    visited.remove((i, j))


def find_zero(grid, zeros_visited):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and (i, j) not in zeros_visited:
                return i, j
    return None, None


if __name__ == "__main__":
    main()
