def main():
    file_path = 'input.txt'

    garden = []
    visited_count = set()
    visited_perimeter = set()

    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            garden.append(line.strip())

    total_perimeter = 0
    total_count = 0
    total_price = 0

    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if (i, j) not in visited_count:
                letter = garden[i][j]
                count = count_plant(letter, garden, visited_count, i, j)
                perimeter = count_perimeter(letter, garden, visited_perimeter, i, j)
                total_count += count
                total_perimeter += perimeter
                total_price += count * perimeter
                

    print("THE ANSWER IS:", total_price)


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


def count_perimeter(letter, garden, visited, i, j, perimeter=0):
    if i < 0 or i >= len(garden) or j < 0 or j >= len(garden[i]):
        return perimeter
    if (i, j) in visited:
        return perimeter
    if garden[i][j] != letter:
        return perimeter

    visited.add((i, j))

    if i + 1 >= len(garden) or garden[i+1][j] != letter:
        perimeter += 1
    if j + 1 >= len(garden[i]) or garden[i][j+1] != letter:
        perimeter += 1
    if i - 1 < 0 or garden[i-1][j] != letter:
        perimeter += 1
    if j - 1 < 0 or garden[i][j-1] != letter:
        perimeter += 1

    perimeter = count_perimeter(letter, garden, visited, i+1, j, perimeter)
    perimeter = count_perimeter(letter, garden, visited, i-1, j, perimeter)
    perimeter = count_perimeter(letter, garden, visited, i, j+1, perimeter)
    perimeter = count_perimeter(letter, garden, visited, i, j-1, perimeter)

    return perimeter


if __name__ == "__main__":
    main()
