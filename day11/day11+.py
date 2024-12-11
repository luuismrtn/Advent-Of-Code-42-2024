def main():
    file_path = 'input.txt'

    rocks = []
    resolved = {}

    with open(file_path, 'r') as f:
        rocks = f.readline().strip().split(" ")
        rocks = list(map(int, rocks))

    result = sum(solve(rock, 75, resolved) for rock in rocks)

    print("THE ANSWER IS:", result)


def solve(stone, blinks, resolved):
    if blinks == 0:
        return 1
    elif (stone, blinks) in resolved:
        return resolved[(stone, blinks)]
    elif stone == 0:
        val = solve(1, blinks - 1, resolved)
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        val = solve(int(str(stone)[:mid]), blinks - 1, resolved) + solve(int(str(stone)[mid:]), blinks - 1, resolved)
    else:
        val = solve(stone * 2024, blinks - 1, resolved)

    resolved[(stone, blinks)] = val

    return val


if __name__ == "__main__":
    main()
