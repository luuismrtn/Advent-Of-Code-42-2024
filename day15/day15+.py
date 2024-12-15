
map = []

INS = []

def main():
    file_path = 'input.txt'

    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line[0] == '#':
                map.append(list(line.strip()))
            elif line[0] in "<>^v":
                for i in range(len(line)):
                    if line[i] in "<>^v":
                        INS.append(line[i])

    expand_map()

    x,y = find_bot()

    for i in range(len(INS)):
        move_bot(INS[i], x, y)
        x, y = find_bot()

    print("THE ANSWER IS:", calculate_result())


def calculate_result():
    total_sum = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "[":
                total_sum += 100 * i + j

    return total_sum


def move_bot(dir, x, y):
    if dir == "^":
        if map[y - 1][x] == "#":
            return
        elif map[y - 1][x] == "[" or map[y - 1][x] == "]":
            push_box(dir, x, y, "@")
        else:
            map[y][x] = "."
            map[y - 1][x] = "@"
    elif dir == "v":
        if map[y + 1][x] == "#":
            return
        elif map[y + 1][x] == "[" or map[y + 1][x] == "]":
            push_box(dir, x, y, "@")
        else:
            map[y][x] = "."
            map[y + 1][x] = "@"
    elif dir == "<":
        if map[y][x - 1] == "#":
            return
        elif map[y][x - 1] == "[" or map[y][x - 1] == "]":
            push_box(dir, x, y, "@")
        else:
            map[y][x] = "."
            map[y][x - 1] = "@"
    elif dir == ">":
        if map[y][x + 1] == "#":
            return
        elif map[y][x + 1] == "[" or map[y][x + 1] == "]":
            push_box(dir, x, y, "@")
        else:
            map[y][x] = "."
            map[y][x + 1] = "@"
    else:
        return
    return


def push_box(dir, x, y, letter):
    cajas_a_mover = []

    if dir == "^":
        dx, dy = x, y - 1

        if map[dy][dx] == "[":
            cajas_a_mover.append((dx, dy))
        else:
            cajas_a_mover.append((dx - 1, dy))
            dx -= 1

        i = 0
        while i < len(cajas_a_mover):
            cx, cy = cajas_a_mover[i]
            if map[cy - 1][cx] == "[":
                cajas_a_mover.append((cx, cy - 1))
            elif map[cy - 1][cx] == "]":
                cajas_a_mover.append((cx - 1, cy - 1))
            if map[cy - 1][cx + 1] == "[":
                cajas_a_mover.append((cx + 1, cy - 1))
            i += 1

        for i in range(len(cajas_a_mover)):
            cx, cy = cajas_a_mover[i]
            if map[cy - 1][cx] == "#" or map[cy - 1][cx + 1] == "#":
                return


        if map[dy][dx] != "#" and map[dy][dx + 1] != "#":
            for i in range(len(cajas_a_mover) - 1, -1, -1):
                cx, cy = cajas_a_mover[i]
                map[cy][cx] = "."
                map[cy][cx + 1] = "."
                map[cy - 1][cx] = "["
                map[cy - 1][cx + 1] = "]"

            map[y][x] = "."
            map[y - 1][x] = letter

    elif dir == "v":
        dx, dy = x, y + 1

        if map[dy][dx] == "[":
            cajas_a_mover.append((dx, dy))
        else:
            cajas_a_mover.append((dx - 1, dy))
            dx -= 1

        i = 0
        while i < len(cajas_a_mover):
            cx, cy = cajas_a_mover[i]
            if map[cy + 1][cx] == "[":
                cajas_a_mover.append((cx, cy + 1))
            elif map[cy + 1][cx] == "]":
                cajas_a_mover.append((cx - 1, cy + 1))
            if map[cy + 1][cx + 1] == "[":
                cajas_a_mover.append((cx + 1, cy + 1))
            i += 1

        for i in range(len(cajas_a_mover)):
            cx, cy = cajas_a_mover[i]
            if map[cy + 1][cx] == "#" or map[cy + 1][cx + 1] == "#":
                return

        if map[dy][dx] != "#" and map[dy][dx + 1] != "#":
            for i in range(len(cajas_a_mover) - 1, -1, -1):
                cx, cy = cajas_a_mover[i]
                map[cy][cx] = "."
                map[cy][cx + 1] = "."
                map[cy + 1][cx] = "["
                map[cy + 1][cx + 1] = "]"

            map[y][x] = "."
            map[y + 1][x] = letter


    elif dir == "<":
        dx, dy = x - 2, y
        
        while map[dy][dx] == "[":
            cajas_a_mover.append((dx, dy))
            dx -= 2
        dx += 1
        if map[dy][dx] == "#":
            return
        
        if map[dy][dx] != "#":
            for i in range(len(cajas_a_mover) - 1, -1, -1):
                cx, cy = cajas_a_mover[i]
                map[cy][cx+1] = "."
                map[cy][cx] = "]"
                map[cy][cx - 1] = "["
            
            map[y][x] = "."
            map[y][x - 1] = letter
    
    elif dir == ">":
        dx, dy = x + 1, y

        while map[dy][dx] == "[":
            cajas_a_mover.append((dx, dy))
            dx += 2

        if map[dy][dx] == "#":
            return

        for i in range(len(cajas_a_mover) - 1, -1, -1):
            cx, cy = cajas_a_mover[i]
            map[cy][cx] = "."
            map[cy][cx + 1] = "["
            map[cy][cx + 2] = "]"

        map[y][x] = "."
        map[y][x + 1] = letter



def find_bot():
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in "@":
                return (j , i)

    return None


def expand_map():
    global map
    expanded_map = []

    for row in map:
        new_row = []
        
        for tile in row:
            if tile == '#':
                new_row.extend(['#', '#'])
            elif tile == 'O':
                new_row.extend(['[', ']'])
            elif tile == '.':
                new_row.extend(['.', '.'])
            elif tile == '@':
                new_row.extend(['@', '.'])
            else:
                new_row.extend([tile, tile])
        
        expanded_map.append(new_row)
    
    map = expanded_map
    

if __name__ == "__main__":
    main()