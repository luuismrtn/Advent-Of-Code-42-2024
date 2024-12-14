import re

def main():
    file_path = 'input.txt'

    height = 103
    width = 101

    pos_robots = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            robot = parse_robot(line)
            if robot != (None, None):
                pos_robots.append(move100(robot, height, width))

    a,b,c,d = count_robots(pos_robots, height, width)

    print("THE ANSWER IS:", a * b * c * d)


def move100(robot, height, width):
    pos, vel = robot
    for _ in range(100):
        pos = (pos[0] + vel[0], pos[1] + vel[1])
        pos = (pos[0] % width, pos[1] % height)
    return pos

def count_robots(robots, height, width):
    a = 0
    b = 0
    c = 0
    d = 0

    middle_x = width // 2
    middle_y = height // 2

    for robot in robots:
        if robot[0] < middle_x and robot[1] < middle_y:
            a += 1
        elif robot[0] < middle_x and robot[1] > middle_y:
            b += 1
        elif robot[0] > middle_x and robot[1] < middle_y:
            c += 1
        elif robot[0] > middle_x and robot[1] > middle_y:
            d += 1
    return a, b, c, d
            

def parse_robot(linea):
    regex = r"p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)"
    match = re.search(regex, linea)
    
    if match:
        pos = (int(match.group(1)), int(match.group(2)))
        vel = (int(match.group(3)), int(match.group(4)))
        return pos, vel
    else:
        return None, None



if __name__ == "__main__":
    main()
