import time

def can_decompose(towel, patterns):
    if not towel:
        return True

    for pat in patterns:
        if towel.startswith(pat):
            if can_decompose(towel[len(pat):], patterns):
                return True

    return False

def main():
    file_path = 'input.txt'

    with open(file_path, 'r') as f:
        lines = f.readlines()

        patterns = lines[0].strip().split(", ")
        towels = [line.strip() for line in lines[2:]]

        counter = 0

    for towel in towels:
        if can_decompose(towel, patterns):
            counter += 1

        print("THE ANSWER IS:", counter)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")
