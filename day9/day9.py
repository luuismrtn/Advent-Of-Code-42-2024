def main():
    file_path = 'input.txt'

    disk = []

    with open(file_path, 'r') as f:
        line = f.readline().strip()
        disk.extend(list(line))

    visual_disk = transform_disk(disk)

    filled_disk = fill_disk(visual_disk)

    total_sum = calculate_sum(filled_disk)
    
    print("THE ANSWER IS:", total_sum)


def transform_disk(disk):
    visual_disk = []
    i = 0
    j = 0
    while i < len(disk):
        num1 = int(disk[i])
        visual_disk.extend([j] * num1)
        i += 1
        if i < len(disk):
            num2 = int(disk[i])
            visual_disk.extend(["."] * num2)
        i += 1
        j += 1
    return visual_disk


def fill_disk(visual_disk):
    i = 0
    while i < len(visual_disk):
        while i < len(visual_disk) and visual_disk[i] != ".":
            i += 1

        if i >= len(visual_disk):
            break

        num, j = find_last_num(visual_disk)

        if j < i:
            break

        visual_disk[j] = "."
        visual_disk[i] = num
        i += 1

    return visual_disk


def find_last_num(visual_disk):
    i = len(visual_disk) - 1
    while visual_disk[i] == ".":
        i -= 1
    return visual_disk[i], i

def calculate_sum(filled_disk):
    sum = 0
    i = 0
    while filled_disk[i] != ".":
        sum += (int(filled_disk[i]) * i)
        i += 1
    return sum

if __name__ == "__main__":
    main()

