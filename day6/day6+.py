def main():
    file_path = 'input.txt'

    grid = []
    obstacles = set()

    with open(file_path, 'r') as f:
        for line in f:
            grid.append(line.strip())

    guard = find_guard(grid)

    if guard is None:
        return

    while True:
        i, j, d, out, loop = move_guard(grid, guard)
        if out:
            break
        if loop:
            if d == "up":
                obstacles.add((i - 1, j))
            elif d == "down":
                obstacles.add((i + 1, j))
            elif d == "left":
                obstacles.add((i, j - 1))
            elif d == "right":
                obstacles.add((i, j + 1))
        guard = (i, j, d)

    print("THE ANSWER IS:", len(obstacles))


def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return (i, j, "up")
            elif grid[i][j] == 'v':
                return (i, j, "down")
            elif grid[i][j] == '<':
                return (i, j, "left")
            elif grid[i][j] == '>':
                return (i, j, "right")
    return None
    

def move_guard(grid, guard):
    i, j, d = guard

    while True:

        next_i, next_j = move_guard_dir(i, j, d)

        if next_i < 0 or next_i >= len(grid) or next_j < 0 or next_j >= len(grid[next_i]):
            return i, j, d, True, False
        
        if grid[next_i][next_j] == '#':
            break

        i, j = next_i, next_j

        if check_loop(grid, i, j, d):
            return i, j, d, False, True
        
    d = change_direction(d)
    return i, j, d, False, False


def check_loop(grid, i, j, dir):
    grid_with_obstacle = [list(row) for row in grid]

    if dir == "up" and i > 0:
        if grid[i - 1][j] != '#':
            grid_with_obstacle[i - 1][j] = '#'
        else:
            return False
    elif dir == "down" and i < len(grid) - 1:
        if grid[i + 1][j] != '#':
            grid_with_obstacle[i + 1][j] = '#'
        else:
            return False
    elif dir == "left" and j > 0:
        if grid[i][j - 1] != '#':
            grid_with_obstacle[i][j - 1] = '#'
        else:
            return False
    elif dir == "right" and j < len(grid[0]) - 1:
        if grid[i][j + 1] != '#':
            grid_with_obstacle[i][j + 1] = '#'
        else:
            return False

    return check_loop_grid(grid_with_obstacle, i, j, dir)


def check_loop_grid(grid, i, j, d):
    visited = set()

    while True:
        if (i, j, d) in visited:
            return True

        visited.add((i, j, d))

        next_i, next_j = move_guard_dir(i, j, d)

        if next_i < 0 or next_i >= len(grid) or next_j < 0 or next_j >= len(grid[next_i]):
            return False

        if grid[next_i][next_j] == '#':
            d = change_direction(d)
        else:
            i, j = next_i, next_j

def move_guard_dir(i, j, d):
    if d == "up":
        return i - 1, j
    elif d == "down":
        return i + 1, j
    elif d == "left":
        return i, j - 1
    elif d == "right":
        return i, j + 1

def change_direction(d):
    if d == "up":
        return "right"
    elif d == "down":
        return "left"
    elif d == "left":
        return "up"
    elif d == "right":
        return "down"

if __name__ == "__main__":
    main()
