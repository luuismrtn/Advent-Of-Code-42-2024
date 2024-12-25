import heapq
import time

class PathFinder:
    def __init__(self, map_data):
        self.MAP = map_data
        self.ROWS = len(map_data)
        self.COLS = len(map_data[0])
        self.DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

    def find_start_end(self):
        for y in range(self.ROWS):
            for x in range(self.COLS):
                if self.MAP[y][x] == 'S':
                    start = (y, x)
                elif self.MAP[y][x] == 'E':
                    end = (y, x)
        return start, end

    def create_segment(self, a, b, c, d):
        return tuple(v for t in sorted([(a,b), (c,d)]) for v in t)

    def count_segments(self, segment_set):
        total = 0
        points = set()
        for a, b, c, d in segment_set:
            total += abs(a-c) + abs(b-d) + 1 - ((a,b) in points) - ((c,d) in points)
            points.update({(a,b), (c,d)})
        return total

    def find_paths(self):
        start, end = self.find_start_end()
        
        distances = {}
        distances[(*start, 1)] = (0, set())
        
        queue = [(0, *start, 1)]
        
        while queue:
            dist, py, px, di = heapq.heappop(queue)
            _, p_set = distances.get((py, px, di), (float("inf"), set()))
            
            for ndi in range(-1, 2):
                diy, dix = self.DIRECTIONS[(di + ndi) % 4]
                npy, npx = py + diy, px + dix
                ndist = dist + 1 + 1000 * (ndi != 0)
                
                while (0 <= npy < self.ROWS and 0 <= npx < self.COLS and
                       self.MAP[npy][npx] != "#" and
                       0 <= npy+dix < self.ROWS and 0 <= npx+diy < self.COLS and
                       0 <= npy-dix < self.ROWS and 0 <= npx-diy < self.COLS and
                       self.MAP[npy+dix][npx+diy] == "#" and
                       self.MAP[npy-dix][npx-diy] == "#"):
                    npy, npx = npy + diy, npx + dix
                    ndist += 1
                
                nset = p_set | {self.create_segment(py, px, npy, npx)}
                
                if (npy, npx) == end:
                    return (ndist, self.count_segments(nset))
                
                if (0 <= npy < self.ROWS and 0 <= npx < self.COLS and
                    self.MAP[npy][npx] != "#"):
                    key = (npy, npx, (di + ndi) % 4)
                    o_dist, o_set = distances.get(key, (float("inf"), set()))
                    
                    if o_dist == ndist:
                        if any(pos not in o_set for pos in nset):
                            o_set.update(nset)
                            heapq.heappush(queue, (ndist, npy, npx, (di + ndi) % 4))
                    elif o_dist > ndist:
                        distances[key] = (ndist, nset)
                        heapq.heappush(queue, (ndist, npy, npx, (di + ndi) % 4))


def main():
    file_path = 'input.txt'
    
    with open(file_path, 'r') as f:
        map_data = [list(line.strip()) for line in f]
    
    path_finder = PathFinder(map_data)
    _, unique_tiles = path_finder.find_paths()
    
    print("THE ANSWER IS:", unique_tiles)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")