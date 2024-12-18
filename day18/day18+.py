import heapq
import time


def get_map_with_bytes(bytes_coords, bytes_map, num_bytes):
    for i in range(num_bytes):
        x, y = bytes_coords[i]
        bytes_map[y][x] = "#"
    return bytes_map
    

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(point, map_bytes):
    height, width = len(map_bytes), len(map_bytes[0])
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dx, dy in directions:
        new_x, new_y = point[0] + dx, point[1] + dy
        
        if (0 <= new_x < width and 
            0 <= new_y < height and 
            map_bytes[new_y][new_x] != "#"):
            neighbors.append((new_x, new_y))
    
    return neighbors


def find_best_path(map_bytes, start, end):

    closed_set = set()
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    came_from = {}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return len(path)
        
        closed_set.add(current)
        
        for neighbor in get_neighbors(current, map_bytes):
            if neighbor in closed_set:
                continue
            
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in [i[1] for i in open_set]:
                heapq.heappush(open_set, (float('inf'), neighbor))
            
            if tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue
            
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
            
            for i, (_, node) in enumerate(open_set):
                if node == neighbor:
                    open_set[i] = (f_score[neighbor], neighbor)
                    heapq.heapify(open_set)
                    break
    
    return -1


def main():
    file_path = 'input.txt'

    bytes_coords = []
    
    HEIGHT = 71
    WIDTH = 71
    num_bytes = 2024

    bytes_map = [["." for _ in range(HEIGHT)] for _ in range(WIDTH)]

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip().split(",")
            bytes_coords.append(tuple(map(int, line)))

    
    while True:
        min_steps = find_best_path(get_map_with_bytes(bytes_coords, bytes_map, num_bytes), (0, 0), (HEIGHT - 1, WIDTH - 1))
        if min_steps == -1:
            break
        num_bytes += 1


    print("THE ANSWER IS:", bytes_coords[num_bytes - 1])


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")