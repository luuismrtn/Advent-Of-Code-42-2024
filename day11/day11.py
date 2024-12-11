def main():
    file_path = 'input.txt'

    rocks = []

    with open(file_path, 'r') as f:
        rocks = f.readline().strip().split(" ")
        rocks = list(map(int, rocks))

    for _ in range(25):
        blink(rocks)

    print("THE ANSWER IS:", len(rocks))

def blink(rocks):
    i = 0
    while i < len(rocks):
        if rocks[i] == 0:
            rocks[i] = 1
        elif len(str(rocks[i])) % 2 == 0:
            num = rocks[i]
            length = len(str(num))
            divisor = 10 ** (length / 2)
            rocks[i] = int(num / divisor)
            rocks.insert(i + 1, (int(num % divisor)))
            i += 1
        else:
            rocks[i] *=  2024
        i += 1

if __name__ == "__main__":
    main()

