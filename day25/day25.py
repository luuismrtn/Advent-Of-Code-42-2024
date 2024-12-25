import time

def transform_schema(schema):
    lock = False
    width = len(schema[0])
    column_counts = [0] * width

    if schema[0][0] == '#':
        lock = True
    
    for column in range(width):
        for row in range(len(schema)):
            if schema[row][column] == '#':
                column_counts[column] += 1

    for num in range(len(column_counts)):
        column_counts[num] -= 1
    
    return column_counts, lock


def find_locks(key, locks):
    locks_count = 0
    for i in range(len(locks)):
        if key[0] + locks[i][0] <= 5 and key[1] + locks[i][1] <= 5 and key[2] + locks[i][2] <= 5 and key[3] + locks[i][3] <= 5 and key[4] + locks[i][4] <= 5:
            locks_count += 1

    return locks_count


def main():
    schematics_key = []
    schematics_lock = []
    current_block = []
    
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if line:
            current_block.append(line)
        elif current_block:
            heights, l = transform_schema(current_block)
            if l:
                schematics_lock.append(heights)
            else:
                schematics_key.append(heights)
            current_block = []
    
    if current_block:
        heights, l = transform_schema(current_block)
        if l:
            schematics_lock.append(heights)
        else:
            schematics_key.append(heights)

    result = 0

    for key in schematics_key:
        result += find_locks(key, schematics_lock)

    print("THE ANSWER IS:", result)
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")