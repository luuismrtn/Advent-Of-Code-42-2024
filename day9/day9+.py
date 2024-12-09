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
    i = len(visual_disk) - 1
    while True:
        num, start_index, length = find_last_num(visual_disk, i)

        if num is None:
            break

        start_space = find_space(visual_disk, length, start_index)

        if start_space != -1:
            for k in range(length):
                visual_disk[start_space + k] = num

            for k in range(start_index + 1, start_index + length + 1):
                visual_disk[k] = "."

        i = start_index

    return visual_disk


def find_last_num(visual_disk, i):
    while i >= 0 and visual_disk[i] == ".":
        i -= 1

    if i < 0:
        return None, None, None

    num = visual_disk[i]
    length = 0

    while i >= 0 and visual_disk[i] == num:
        i -= 1
        length += 1

    return num, i, length


def find_space(visual_disk, length, index):
    i = 0
    while i < index + 1:
        start_i = i

        while i < len(visual_disk) and visual_disk[i] == ".":
            i += 1

        if (i - start_i) >= length:
            return start_i

        i += 1

    return -1


def calculate_sum(filled_disk):
    total_sum = 0
    for i, value in enumerate(filled_disk):
        if value != ".":
            total_sum += int(value) * i
    return total_sum


if __name__ == "__main__":
    main()
