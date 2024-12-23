def main():
    file_path = 'input.txt'

    garden = []

    with open(file_path, 'r') as f:
        for line in f:
            garden.append(list(line.strip()))

    garden_copy = [row[:] for row in garden]
   
    total_price = 0
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j] != '#':
                total_price += process_region(garden, garden_copy, i, j)
   
    print("THE ANSWER IS:", total_price)


def in_bounds(garden, r, c):
    return 0 <= r < len(garden) and 0 <= c < len(garden[r])


def count_sides(garden, garden_copy, row, col):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
   
    sides = 0
    letter = garden_copy[row][col]
   
    for i in range(4):
        new_r = row + dr[i]
        new_c = col + dc[i]
        
        if not in_bounds(garden, new_r, new_c) or garden_copy[new_r][new_c] != letter:
            prev_r = row + dr[(i - 1) % 4]
            prev_c = col + dc[(i - 1) % 4]
            is_start_edge = not in_bounds(garden, prev_r, prev_c) or garden_copy[prev_r][prev_c] != letter
            
            corner_r = new_r + dr[(i - 1) % 4]
            corner_c = new_c + dc[(i - 1) % 4]
            is_concave = in_bounds(garden, corner_r, corner_c) and garden_copy[corner_r][corner_c] == letter
            
            if is_start_edge or is_concave:
                sides += 1
    
    return sides


def count_plant(letter, garden, visited, i, j, count=0):
    if i < 0 or i >= len(garden) or j < 0 or j >= len(garden[i]):
        return count
    if (i, j) in visited:
        return count
    if garden[i][j] != letter:
        return count

    visited.add((i, j))
    count += 1

    count = count_plant(letter, garden, visited, i+1, j, count)
    count = count_plant(letter, garden, visited, i-1, j, count)
    count = count_plant(letter, garden, visited, i, j+1, count)
    count = count_plant(letter, garden, visited, i, j-1, count)

    return count


def process_region(garden, garden_copy, start_r, start_c):
    total_sides = count_sides(garden, garden_copy, start_r, start_c)
    letter = garden[start_r][start_c]
    area = count_plant(letter, garden, set(), start_r, start_c)
    
    return area * total_sides


if __name__ == "__main__":
    main()