from itertools import combinations
from collections import deque
import time


def find_start_end(map_data):
    for y in range(len(map_data)):
        for x in range(len(map_data[0])):
            if map_data[y][x] == 'S':
                return (x, y)


def main():
    file_path = 'input.txt'

    with open(file_path, 'r') as f:
        map_data = [list(line.strip()) for line in f]

    start = find_start_end(map_data)

    dist = {start: 0}
    todo = deque([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while todo:
        x, y = todo.popleft()
        for dx, dy in directions:
            new = (x + dx, y + dy)
            if (0 <= new[1] < len(map_data) and
                0 <= new[0] < len(map_data[0]) and
                map_data[new[1]][new[0]] != '#' and
                new not in dist):
                dist[new] = dist[(x, y)] + 1
                todo.append(new)

    sol = 0

    for (p, i), (q, j) in combinations(dist.items(), 2):
        d = abs(p[0] - q[0]) + abs(p[1] - q[1])
        if d == 2 and j - i - d >= 100:
            sol += 1


    print("THE ANSWER IS:", sol)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")