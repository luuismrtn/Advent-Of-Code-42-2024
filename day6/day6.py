def main():
    file_path = 'input.txt'

    grid = []
    sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            grid.append(line.strip())

    guard = find_guard(grid)

    if guard is None:
        return

    while True:
        i, j, d, steps, out = move_guard(grid, guard)
        if out:
            sum += steps
            break

        sum += steps
        guard = (i, j, d)

    print("THE ANSWER IS:", sum)


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
    steps = 0

    while True:
        next_i, next_j = i, j
        if d == "up":
            next_i -= 1
        elif d == "down":
            next_i += 1
        elif d == "left":
            next_j -= 1
        elif d == "right":
            next_j += 1

        if next_i < 0 or next_i >= len(grid) or next_j < 0 or next_j >= len(grid[next_i]):
            return i, j, d, steps, True
        
        if grid[next_i][next_j] == '#':
            break

        i, j = next_i, next_j
        if grid[i][j] != 'X':
            grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]
            steps += 1

    if d == "up":
        d = "right"
    elif d == "down":
        d = "left"
    elif d == "left":
        d = "up"
    elif d == "right":
        d = "down"

    return i, j, d, steps, False

if __name__ == "__main__":
    main()


#Respuestas: (6,3), (7,6), (7,7), (8,1), (8,3), (9,7)
