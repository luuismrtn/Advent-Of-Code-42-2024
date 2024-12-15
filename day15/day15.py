
MAP = []

INS = []

def main():
    file_path = 'input.txt'

    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line[0] == '#':
                MAP.append(list(line.strip()))
            elif line[0] in "<>^v":
                for i in range(len(line)):
                    if line[i] in "<>^v":
                        INS.append(line[i])

    x,y = find_bot()

    for i in range(len(INS)):
        move_bot(INS[i], x, y)
        x, y = find_bot()

    total_sum = calculate_result()

    print("THE ANSWER IS:", total_sum)

def calculate_result():
    total_sum = 0
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] == "O":
                total_sum += 100 * i + j

    return total_sum


def move_bot(dir, x, y):
    if dir == "^":
        if MAP[y - 1][x] == "#":
            return
        elif MAP[y - 1][x] == "O":
            push_box(dir, x, y, "@")
        else:
            MAP[y][x] = "."
            MAP[y - 1][x] = "@"
    elif dir == "v":
        if MAP[y + 1][x] == "#":
            return
        elif MAP[y + 1][x] == "O":
            push_box(dir, x, y, "@")
        else:
            MAP[y][x] = "."
            MAP[y + 1][x] = "@"
    elif dir == "<":
        if MAP[y][x - 1] == "#":
            return
        elif MAP[y][x - 1] == "O":
            push_box(dir, x, y, "@")
        else:
            MAP[y][x] = "."
            MAP[y][x - 1] = "@"
    elif dir == ">":
        if MAP[y][x + 1] == "#":
            return
        elif MAP[y][x + 1] == "O":
            push_box(dir, x, y, "@")
        else:
            MAP[y][x] = "."
            MAP[y][x + 1] = "@"
    else:
        return
    return


def push_box(dir, x, y, letter):
    cajas_a_mover = []
    if dir == "^":
        dx, dy = x, y - 1

        while MAP[dy][dx] == "O":
            cajas_a_mover.append((dx, dy))
            dy -= 1
        
        if MAP[dy][dx] != "#":
            for i in range(len(cajas_a_mover) - 1, -1, -1):
                cx, cy = cajas_a_mover[i]
                MAP[cy][cx] = "."
                MAP[cy - 1][cx] = "O"
            
            MAP[y][x] = "."
            MAP[y - 1][x] = letter
        
    elif dir == "v":
        dx, dy = x, y + 1
        
        while MAP[dy][dx] == "O":
            cajas_a_mover.append((dx, dy))
            dy += 1
        
        if MAP[dy][dx] != "#":
            for i in range(len(cajas_a_mover) - 1, -1, -1):
                cx, cy = cajas_a_mover[i]
                MAP[cy][cx] = "."
                MAP[cy + 1][cx] = "O"
            
            MAP[y][x] = "."
            MAP[y + 1][x] = letter
        
    elif dir == "<":
        dx, dy = x - 1, y
        
        while MAP[dy][dx] == "O":
            cajas_a_mover.append((dx, dy))
            dx -= 1
        
        if MAP[dy][dx] != "#":
            for i in range(len(cajas_a_mover) - 1, -1, -1):
                cx, cy = cajas_a_mover[i]
                MAP[cy][cx] = "."
                MAP[cy][cx - 1] = "O"
            
            MAP[y][x] = "."
            MAP[y][x - 1] = letter
        
    elif dir == ">":
        dx, dy = x + 1, y
        
        while MAP[dy][dx] == "O":
            cajas_a_mover.append((dx, dy))
            dx += 1
        
        if MAP[dy][dx] != "#":
            for i in range(len(cajas_a_mover) - 1, -1, -1):
                cx, cy = cajas_a_mover[i]
                MAP[cy][cx] = "."
                MAP[cy][cx + 1] = "O"
            
            MAP[y][x] = "."
            MAP[y][x + 1] = letter


def find_bot():
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] in "@":
                return (j , i)

    return None


if __name__ == "__main__":
    main()