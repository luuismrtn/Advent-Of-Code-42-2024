import heapq
import time

class PathFinder:
    def __init__(self, map_data):
        self.MAP = map_data
        self.ROWS = len(map_data)
        self.COLS = len(map_data[0])


    def is_valid_move(self, x, y):
        return self.MAP[y][x] != '#'
    
    
    def find_start_end(self):
        start, end = None, None
        for y in range(self.ROWS):
            for x in range(self.COLS):
                if self.MAP[y][x] == 'S':
                    start = (x, y)
                elif self.MAP[y][x] == 'E':
                    end = (x, y)
                if start and end:
                    return start, end
        return start, end

    
    def calculate_path_cost(self, path):
        direction_changes = 0
        for i in range(1, len(path)):
            if path[i-1][2] != path[i][2]:
                direction_changes += 1000
        
        base_path_cost = len(path) + direction_changes
        return base_path_cost
    
    
    def a_star_search(self):
        start, end = self.find_start_end()
        
        DIRECTIONS = [
            (1, 0, "E"),
            (-1, 0, "W"),
            (0, 1, "S"),
            (0, -1, "N")
        ]
        
        # open_set: (f_score, g_score, current_pos, path)
        open_set = []
        heapq.heappush(open_set, (0, 0, start, [(start[0], start[1], "E")]))
        
        best_score = float('inf')
        best_path = None
        
        closed_set = set()
        
        while open_set:
            f_score, g_score, current, path = heapq.heappop(open_set)
            
            if f_score >= best_score:
                continue
            
            if current == end:
                path_cost = self.calculate_path_cost(path)
                if path_cost < best_score:
                    best_score = path_cost
                    best_path = path
                continue
            
            state_key = (current, path[-1][2])
            if state_key in closed_set:
                continue
            closed_set.add(state_key)
            
            for dx, dy, new_dir in DIRECTIONS:
                next_x, next_y = current[0] + dx, current[1] + dy
                
                if not self.is_valid_move(next_x, next_y):
                    continue
                
                new_path = path + [(next_x, next_y, new_dir)]
                
                new_g_score = g_score + 1
                f_score = self.calculate_path_cost(new_path)
                
                heapq.heappush(open_set, (f_score, new_g_score, (next_x, next_y), new_path))
        
        return best_path, best_score - 1


def main():
    file_path = 'input.txt'

    with open(file_path, 'r') as f:
        map_data = [list(line.strip()) for line in f]
    
    path_finder = PathFinder(map_data)
    _, best_score = path_finder.a_star_search()


    print("THE ANSWER IS:", best_score)


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")