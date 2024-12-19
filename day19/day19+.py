import time


def count_combinations(towel, patterns, memo):
    if towel in memo:
        return memo[towel]
    if not towel:
        return 1

    total_count = 0
    for pat in patterns:
        if towel.startswith(pat):
            total_count += count_combinations(towel[len(pat):], patterns, memo)

    memo[towel] = total_count
    return total_count


def main():
    file_path = "input.txt"

    total_combinations = 0

    with open(file_path, "r") as f:
        lines = f.readlines()

        patterns = lines[0].strip().split(", ")
        towels = [line.strip() for line in lines[2:]]

    for towel in towels:
        memo = {}
        total_combinations += count_combinations(towel, patterns, memo)


    print("THE ANSWER IS:", total_combinations)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")
