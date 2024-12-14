import re

HEIGHT = 103
WIDTH = 101

def main():
    file_path = 'input.txt'
    pos_robots = []
    sec = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            robot = parse_robot(line)
            if robot != (None, None):
                pos_robots.append(robot)

    while is_christmas_tree(pos_robots) == False:
        for i in range(len(pos_robots)):
            pos, vel = pos_robots[i]
            pos_robots[i] = move1(pos, vel)
        sec += 1

    print("THE ANSWER IS:", sec)

def is_christmas_tree(robots):
    robot_positions = set(pos for pos, _ in robots)

    MIN_RECT_HEIGHT = 5
    MIN_RECT_WIDTH = 15
    MIN_DENSITY = 0.7

    accum = [[0] * (WIDTH + 1) for _ in range(HEIGHT + 1)]
    for x, y in robot_positions:
        accum[y + 1][x + 1] = 1

    for i in range(1, HEIGHT + 1):
        for j in range(1, WIDTH + 1):
            accum[i][j] += accum[i - 1][j] + accum[i][j - 1] - accum[i - 1][j - 1]

    for i in range(HEIGHT - MIN_RECT_HEIGHT + 1):
        for j in range(WIDTH - MIN_RECT_WIDTH + 1):
            x1, y1 = j, i
            x2, y2 = j + MIN_RECT_WIDTH, i + MIN_RECT_HEIGHT

            occupied_cells = accum[y2][x2] - accum[y1][x2] - accum[y2][x1] + accum[y1][x1]
            total_cells = MIN_RECT_WIDTH * MIN_RECT_HEIGHT

            density = occupied_cells / total_cells
            if density >= MIN_DENSITY:
                return True

    return False

def move1(pos, vel):
    new_pos = (pos[0] + vel[0], pos[1] + vel[1])
    new_pos = (new_pos[0] % WIDTH, new_pos[1] % HEIGHT)
    return (new_pos, vel)

def parse_robot(linea):
    regex = r"p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)"
    match = re.search(regex, linea)

    if match:
        pos = (int(match.group(1)), int(match.group(2)))
        vel = (int(match.group(3)), int(match.group(4)))
        return (pos, vel)
    else:
        return None, None

if __name__ == "__main__":
    main()